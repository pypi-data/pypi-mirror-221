"""
Database of interaction models and samples for classical molecular
dynamics and Monte Carlo simulations

Note: accessing the database should only be done via the public,
read-only API defined below. Inserting new entries on a checked-out
database should only be done for registering new database or samples
in the official repository.
"""

import os
import glob
import json
import tempfile
import shutil
import hashlib
from copy import deepcopy
from .helpers import _wget
from . import f90, rumd, hooks
from .database import _TinyDB, Database, Query
from .helpers import pprint, copy
from .schema import schema_version, schemas
from .hooks import version

_root = os.path.dirname(__file__)
default_schema_version = 1

# Databases
samples = Database(os.path.join(_root, "_samples.json"))
samples.storage_path = 'storage/{model}/{version}_{md5_hash}'
models = _TinyDB(os.path.join(_root, "_models.json"))
models.require = ('name', 'version', 'schema_version')  # or state?

# Default query
query = Query()

# Public API

def model(name, version=0, schema_version=None):
    """
    Return database matching `name` and optionally `version`.

    The default `version` is 0 (original model); setting
    `version=None` will return a list of all matching database.
    """
    def _capitalize(name):
        return '-'.join([entry.capitalize() for entry in name.split('_')])
    if schema_version is None:
        schema_version = default_schema_version
        
    matches = models.search(((query.name == name) | (query.name == _capitalize(name))) &
                             (query.version == version) &
                             (query.schema_version == schema_version))
    if len(matches) == 0:
        raise KeyError(f'Model {name} not found with schema {schema_version}')
    return matches[0]

def sample(path):
    """
    Return a single sample matching the path
    """
    matches = samples.search(query.path == path)
    if len(matches) == 0:
        raise KeyError(f'Model {name} not found with schema {schema_version}')
    return matches[0]

# Potentials and cutoffs

# TODO: implement add() method with checks on existence
from inspect import getmembers, isfunction, isclass
from .helpers import _objdict
from . import _potentials
from . import _cutoffs

potentials = _objdict()
for name, func in getmembers(_potentials, isfunction):
    potentials[name] = func

cutoffs = _objdict()
for name, cls in getmembers(_cutoffs, isclass):
    cutoffs[name] = cls

def potential(name):
    return potentials[name]
    
def cutoff(name):
    return cutoffs[name]


