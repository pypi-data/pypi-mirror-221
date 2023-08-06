import os
import re
import numpy
from atooms.core.utils import tipify
from atooms.trajectory import Trajectory
from atooms.system.particle import distinct_species, composition
from .helpers import schema_version

def version(entry):
    """Detect schema_version and set default version"""
    schema = schema_version(entry)
    if 'version' not in entry:
        return {'version': 0,
                'schema_version': schema
                }
    else:
        return {'schema_version': schema}

def absolute_path(entry, root):
    """Add absolute path"""
    if entry['path'].startswith('/'):
        return {'absolute_path': entry['path']}
    else:
        return {'absolute_path': os.path.join(root, entry['path'])}
    
def format_extension(entry, format=None):
    path = entry['path']
    if format is None:
        ext = os.path.splitext(path)[-1].strip('.')
        if len(ext) > 0:
            format = ext
    return {
        "format": format,
        "extension": ext
    }

def metadata_from_atooms(entry):
    # TODO: use db['cache'] to gather all caches
    # Cache to avoid fetching data if not necessary
    # TODO: what happens with directories?
    path = entry['absolute_path']
    if not os.path.exists(path):
        # Exit gracefully. This is ok if files are removed and are
        # then cleared with update()
        return {}
        
    last_modified = os.path.getmtime(path)
    if '__cache_metadata_from_atooms' in entry:
        if entry['__cache_metadata_from_atooms'] >= last_modified:
            return {}

    # Store metadata
    th = Trajectory(path)
    system = th[0]
    db = {}
    db['__cache_metadata_from_atooms'] = os.path.getmtime(th.filename)
    s = re.search(r'([a-zA-Z0-9]*)Trajectory([a-zA-Z0-9]*)', str(th.__class__))
    fmt = (s.group(1) + s.group(2)).lower()
    db['format'] = fmt
    db['frames'] = len(th)
    db['megabytes'] = int((os.path.getsize(th.filename) / 1e6))
    db['particles'] = len(system.particle)
    db['species'] = ', '.join(distinct_species(system.particle))
    db['composition'] = dict(composition(system.particle))
    # radii = system.dump('particle.radius')
    # db['size dispersion'] = str((numpy.std(radii) / numpy.mean(radii)))
    db['density'] = round(system.density, 10)
    if system.cell is not None:
        db['cell side'] = str(list(system.cell.side))[1: -1]
        db['cell volume'] = system.cell.volume
    if len(th) > 1:
        db['steps'] = int(th.steps[-1])
        db['duration'] = int(th.times[-1])
        db['timestep'] = float(th.timestep)
        db['block size'] = int(th.block_size)
        db['grandcanonical'] = th.grandcanonical
    th.close()
    return db

def metadata_from_path(entry, aliases=(('T', 'temperature'),
                                       ('P', 'pressure'))):
    path = entry['path']
    db = {}
    for entry in os.path.dirname(path).split('/'):
        for sub in entry.split('_'):
            res = re.match('([a-zA-Z]*)([0-9.]*)', sub)
            if len(res.group(2)) > 0:
                key = res.group(1)
                for alias in aliases:
                    if key == alias[0]:
                        key = alias[1]
                    db[key] = tipify(res.group(2))
    return db
