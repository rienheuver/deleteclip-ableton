#__init__.py
from .DeleteClip import DeleteClip

def create_instance(c_instance):
    return DeleteClip(c_instance)
