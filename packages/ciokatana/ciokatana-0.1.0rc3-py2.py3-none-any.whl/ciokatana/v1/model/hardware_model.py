from ciocore import data as coredata
from ciokatana.v1 import const as k

INSTANCE_TYPE_PARAM = "instanceType"
PREEMPTIBLE_PARAM = "preemptible"
RETRIES_PARAM = "retries"


def create(node):
    """Create the parameters.
    
    To choose the initial instance_type, we look for the first instance type
    with more than 2 cores and more than 8GB of memory. If none is found, we
    just use the first one we find.
    """

    if coredata.valid():
        hardware = coredata.data()["instance_types"]
        instance_type = hardware.find_first( lambda x: float(x["cores"]) > 2 and float(x["memory"]) > 8 )
        if not instance_type:
            instance_type = hardware.find_first( lambda x: True )
    if instance_type:
        instance_type = instance_type["name"]
    else:
        instance_type = k.NOT_CONNECTED

    node.getParameters().createChildString(INSTANCE_TYPE_PARAM, instance_type)
    node.getParameters().createChildNumber(PREEMPTIBLE_PARAM, 1)
    node.getParameters().createChildNumber(RETRIES_PARAM, 1)


def get_value(node):
    return node.getParameter(INSTANCE_TYPE_PARAM).getValue(0)


def set_value(node, value):
    node.getParameter(INSTANCE_TYPE_PARAM).setValue(value, 0)


def resolve(node):
    """Resolve the payload for the node."""
    result = {
        "instance_type": node.getParameter(INSTANCE_TYPE_PARAM).getValue(0),
        "preemptible": node.getParameter(PREEMPTIBLE_PARAM).getValue(0) > 0,
    }
    retries =  int(node.getParameter(RETRIES_PARAM).getValue(0))
    if result["preemptible"] and retries:
        result.update({"autoretry_policy": {"preempted": {"max_retries": retries}}})
    return result
