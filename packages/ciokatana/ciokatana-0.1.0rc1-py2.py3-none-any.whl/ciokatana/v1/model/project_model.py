from ciocore import data as coredata
from ciokatana.v1 import const as k

PROJECT_PARAM = "conductorProject"

def create(node):
    """Create the project parameter on the node.
    
    If we already connected to conductor, use the first project in the list.
    """
    projects = coredata.data()["projects"] if coredata.valid() else []
    
    if projects:
        project = projects[0]
    else:
        project = k.NOT_CONNECTED
    node.getParameters().createChildString(PROJECT_PARAM, project)

# accessors
def get_value(node):
    return node.getParameter(PROJECT_PARAM).getValue(0)

def set_value(node, value):
    node.getParameter(PROJECT_PARAM).setValue(value, 0)

def resolve(node):
    """Resolve the payload field for the project parameter."""
    return {"project": node.getParameter(PROJECT_PARAM).getValue(0)}
