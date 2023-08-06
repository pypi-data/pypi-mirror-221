import os
import shutil
import hashlib
from .schema import schema_version


def pprint(rows, columns=None, sort_by=None, max_rows=10):
    """Pretty print `rows` (a list of dicts)"""
    
    def _tabular(data, max_len=100):
        """General function to format `data` list in tabular table"""
        # Predict formatting
        lens = [0 for _ in range(len(data[0]))]
        for entry in data:
            for i, value in enumerate(entry):
                lens[i] = max(lens[i], len(str(value)))
        fmts = [f'{{:{lens[i]}s}}' for i in range(len(lens))]
        fmt = ' '.join(fmts)

        # Store list of lines
        lines = []
        lines.append(fmt.format(*data[0]))
        lines.append('-'*(sum(lens) + len(lens) - 1))
        for entry in data[1:]:
            entry = [str(_) for _ in entry]
            lines.append(fmt.format(*entry))
            if len(lines) > max_rows and max_rows > 0:
                lines.append(f'... {len(data) - max_rows} entries not shown')
                break

        # Limit columns
        if sum(lens) > max_len:
            for i, line in enumerate(lines):
                if i < 2:
                    fill = '     '
                else:
                    fill = ' ... '
                lines[i] = line[:max_len//2] + fill + line[sum(lens) - max_len//2:]
        return lines

    # Format and sort the data        
    if columns is None:
        columns = set([e for e in rows[0] if not e.startswith('__')])
        for entry in rows:
            new_columns = set([e for e in entry if not e.startswith('__')])
            columns = set.union(columns, new_columns)
        columns = sorted(columns)

    if sort_by is not None:
        if not (isinstance(sort_by, list) or isinstance(sort_by, tuple)):
            sort_by = [sort_by]
        rows = sorted(rows[1:], key=lambda x: [x[_] for _ in sort_by])
  
    # Tabularize lines and join them
    rows = [columns] + [[str(entry.get(key)) for key in columns] for entry in rows]
    lines = _tabular(rows)
    print('\n'.join(lines))

def _wget(url, output_dir):
    """Like wget on the command line"""
    try:
        from urllib.request import urlopen  # Python 3
    except ImportError:
        from urllib2 import urlopen  # Python 2

    basename = os.path.basename(url)
    output_file = os.path.join(output_dir, basename)
    response = urlopen(url)
    length = 16*1024
    with open(output_file, 'wb') as fh:
        shutil.copyfileobj(response, fh, length)


def copy(entry, path='/tmp/{path}', root=''):
    """Get a copy of `path` in the samples database and return the path to it"""
    from atooms.core.utils import mkdir

    # Handle output path
    if path is None:
        # Output path is a temporary directory
        tmpdir = tempfile.mkdtemp()
        basename = os.path.basename(entry['path'])
        path = os.path.join(tmpdir, basename)
    else:
        # Interpolate path with entry fields
        path = path.format(**entry)

    # Now copy
    if entry['path'].startswith('http'):
        # Over the network
        _wget(entry['path'], tmpdir)
    else:
        # Local storage
        mkdir(os.path.dirname(path))
        if entry['path'].startswith('/'):
            # Absolute path, so ignore root variable
            shutil.copy(entry['path'], path)
        else:
            # Path is relative to root, most likely database folder
            shutil.copy(os.path.join(root, entry['path']), path)

    return path

class _objdict(dict):

    """Boots a dict with object-like attribute accessor"""

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]

def add_model_json(path):
    """
    If `path` is a directory, add all json files in there to the
    global `database`. If `path` ends with `json`, it will be assumed
    to be match one or multiple json files (ex. `*.json`).
    """
    if path.endswith('json'):
        search_path = glob.glob(path)
    else:
        search_path = glob.glob('{}/*.json'.format(path))

    for _path in search_path:
        # Read json file
        with open(_path) as fh:
            try:
                model = json.load(fh)
            except (ValueError, json.decoder.JSONDecodeError):
                print('Error reading file {}'.format(_path))
                raise

        # By default, the model name is the file basename (stripped of .json)
        if 'name' not in model:
            name = os.path.basename(_path)[:-5]
            model['name'] = '-'.join([entry.capitalize() for entry in name.split('_')])

        yield model
