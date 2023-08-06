import os
import tempfile
import hashlib
from tinydb import TinyDB, Query
from tinydb.table import Table
from atooms.core.utils import mkdir
from .hooks import absolute_path
from .helpers import _wget, copy, pprint
try:
    from tqdm import tqdm as progress
except:
    progress = lambda x: x

class _TinyDB(TinyDB):

    """
    A custom TinyDB database with read hooks, required variables and
    columns accessor
    """

    def __init__(self, *args, **kwargs):
        if len(args) == 0 and len(kwargs) == 0:
            from tinydb.storages import MemoryStorage
            super().__init__(storage=MemoryStorage)
        else:
            super().__init__(*args, **kwargs)
        self.require = ()
        self._hooks = []

    def add_hook(self, hook, *args, **kwargs):
        """Register a new hook to be applied when accessing the entries"""
        if hook not in [hook[0] for hook in self._hooks]:
            self._hooks.append((hook, args, kwargs))

    def remove_hooks(self):
        """Remove hooks"""
        self._hooks = []

    def _apply_hooks(self, entry):
        """Apply hooks and store the values in the new entry"""
        for hook in self._hooks:
            result = hook[0](entry, *hook[1], **hook[2])
            entry.update(result)
        return entry

    def columns(self, merge=set.intersection):
        """Return columns of database"""
        cols = None
        for entry in self:
            if cols is None:
                cols = set(entry.keys())
            else:
                cols = merge(cols, set(entry.keys()))
        return sorted(list(cols))

    def rows(self, cond=None, columns=(), sort_by=()):
        """
        Return rows matching a condition as dicts with columns as keys,
        sorted according to column keys.
        """
        if cond is None:
            entries = self.all()
        else:
            entries = self.search(cond)

        if sort_by is not None:
            if not (isinstance(sort_by, list) or isinstance(sort_by, tuple)):
                sort_by = [sort_by]
            entries = sorted(entries, key=lambda x: [x[_] for _ in sort_by])

        if len(columns) == 0:
            columns = self.columns()

        output = {}
        for column in columns:
            output[column] = [entry[column] for entry in entries]
        return output

    def pprint(self, cond=None, **kwargs):
        """Pretty print"""
        if cond is None:
            entries = self.all()
        else:
            entries = self.search(cond)
        pprint(entries, **kwargs)

    def insert(self, entry):
        """
        We upsert against the `self.require` variable. If all required
        variables of the new entry match an existing one and overwrite
        is True, then we only update the entry. If overwrite is False,
        an error is raised.
        """
        if len(self.require) == 0:
            # TODO: could not get this with super()
            from tinydb.table import Table
            Table.insert(self, entry)
        else:
            # Make sure that all required variables match
            query = Query()
            queries = []
            for var in self.require:
                queries.append(query[var] == entry[var])
            cond = queries[0]
            for q in queries[1: ]:
                cond = cond.__and__(q)
            self.upsert(entry, cond)

    def update(self):
        """Update database entries, to store metadata from hooks"""
        # This will store metadata from hooks
        for entry in progress(self.all()):
            self.insert(**entry)

    # The following two methods are redefined to allow for readonly
    # hooks that are applied only when accessing the
    # database. Otherwise, we can first store the hooks results in the
    # database (via some update) and get rid of them.

    # TODO: should we keep hooks or just provide decorators to client code?

    # Note: storing absolute paths in a portable way can be achieved by
    # restoring read only hooks, overloading all() and search(). This may
    # also be useful when the db is read only and we do not want to modify
    # it. If we store them upon insertion, the database will not be
    # portable when moving it to a new folder and this is a feature to
    # preserve. We could of course just process the output list in client
    # code, but things like searching for custom columns would not be
    # possible. One possible nomenclature is pre and post hook, like git.

    def __iter__(self):
        """
        Return an iterator for the default table's documents.
        """
        for entry in self.table(self.default_table_name):
            entry = self._apply_hooks(entry)
            yield entry

    def search(self, cond):
        """
        Search for all documents matching a 'where' cond.

        :param cond: the condition to check against
        :returns: list of matching documents
        """
        # TODO: how should we overload this?
        entries = self.table(self.default_table_name).search(cond)
        for entry in entries:
            self._apply_hooks(entry)
        return entries

    def all(self):
        """
        Get all documents stored in the table.

        :returns: a list with all documents.
        """
        return list(iter(self))

class Database(_TinyDB):

    """
    A simple database of files
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Look for the root of the db file, if present
        # This is where we will store the files, if requested
        try:
            path = self._storage._handle.name
            # TODO: perhaps rename root? or privatize?
            self.storage_root = os.path.dirname(path)
            self.add_hook(absolute_path, self.storage_root)
        except AttributeError:
            self.storage_root = None
        self.storage_path = '{md5_hash}'
        self.require = ('md5_hash', )

    def remove_hooks(self):
        """Remove hooks"""
        # Make sure absolute paths are always added
        super().remove_hooks()
        self.add_hook(absolute_path, self.storage_root)

    # TODO: avoid reinsertions if path (exists & hash is the same)
    def insert(self, input_path=None, copy=False, **kwargs):
        """
        Insert a new `input_path` in the database. If `copy` is True, the
        file is copied in the database storage.
        """
        if input_path is None:
            # Useful for update. We assume absolute_path has been added already...
            input_path = kwargs["absolute_path"]

        # Set paths: storage_path is what goes in the db
        if input_path.startswith('http'):
            tmpdir = tempfile.mkdtemp()
            basename = os.path.basename(input_path)
            _wget(input_path, tmpdir)
            local_path = os.path.join(tmpdir, basename)
        else:
            local_path = input_path

        # Read data
        with open(local_path, "rb") as fh:
            data = fh.read()

        # Create the new entry
        # TODO: handle http paths
        entry = {}
        entry.update(**kwargs)
        entry['md5_hash'] = hashlib.md5(data).hexdigest()

        if copy:
            # If storing a local copy, we interpolate the path
            extension = os.path.splitext(local_path)[-1]
            entry['path'] = self.storage_path.format(**entry) + extension
            out_path = os.path.join(self.storage_root, entry["path"])
            with open(out_path, "wb") as fh:
                fh.write(data)
        else:
            # TODO: should we make it absolute? or relative to what?
            entry['path'] = input_path

        # Add the entry to the database
        super().insert(entry)

    def insert_glob(self, path, copy=False, **kwargs):
        """Insert multiple files from a globbale `path`."""
        from glob import glob
        for _path in progress(glob(path, recursive=True)):
            self.insert(_path, copy, **kwargs)

    def insert_multiple(self, path, copy=False, **kwargs):
        """Insert multiple files from an interable `path`"""
        for _path in progress(path):
            self.insert(_path, copy, **kwargs)

    def _missing(self):
        """Check that the paths of all the entries exist"""
        # TODO: handle http links (check if accessible)
        # TODO: this does not work
        # query = Query()
        # return self.search(~ (query.absolute_path.test(os.path.exists)))
        docs = []
        for entry in self.all():
           if not os.path.exists(entry['absolute_path']):
               docs.append(entry)
        return docs

    def update(self):
        """
        Update database entries, clearing missing files and storing
        updated metadata from hooks
        """
        # Files that have been deleted are removed from the db
        #query = Query()
        #return self.search(~ (query.absolute_path.test(os.path.exists)))
        ids = []
        for entry in self.all():
           if not os.path.exists(entry['absolute_path']):
               ids.append(entry.doc_id)
        self.remove(doc_ids=ids)
        # if len(ids) > 0:
        #     print(f"{len(ids)} entries will be removed")
        # Now update the rest of the entries
        super().update()

    def copy(self, query, path='/tmp/{path}'):
        """Get copies entries matching `query` in the database and return the paths"""
        paths = []
        for entry in self.search(query):
            out_path = copy(entry, root=self.storage_root)
            paths.append(out_path)
        return paths
