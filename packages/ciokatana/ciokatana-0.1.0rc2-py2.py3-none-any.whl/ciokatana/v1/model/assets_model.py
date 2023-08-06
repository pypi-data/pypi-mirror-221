from Katana import NodegraphAPI
from ciokatana.v1.model import array_model
from ciokatana.v1 import const as k
from ciopath.gpath_list import PathList

PARAM = "extraAssets"


def create(node):
    """Create the project parameter and internal node."""
    params = node.getParameters()

    params.createChildStringArray(PARAM, 0)

def get_entries(node):
    return array_model.get_entries(node, PARAM)


def set_entries(node, entries):
    array_model.set_entries(node, PARAM, entries)


def scan_assets():
    """Scan the nodegraph for assets.
    
    Note: this is a stub."""
    return []


def resolve(node):
    projectfile = NodegraphAPI.NodegraphGlobals.GetProjectFile()
    if not projectfile:
        projectfile = k.NOT_SAVED
    path_list = PathList(projectfile)

    extra_assets = get_entries(node)
    path_list.add(*extra_assets)

    scanned_assets = scan_assets()
    path_list.add(*scanned_assets)
    
    path_list.real_files()

    return {
        "upload_paths": [p.fslash() for p in path_list],
    }
