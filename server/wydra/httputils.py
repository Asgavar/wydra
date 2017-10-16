from typing import Tuple

def extract_path(path: str):
    """
    Extracts resource's name and id from URL.
    Expects it to be only one level deep, but that's not a problem in my case.

    Args:
        path (str): PATH_INFO from WSGI environ.

    Returns:
        resource_name (str)
        resource_id (str)
    """
    path = path.split('/')
    resource_name = path[1]
    resource_id = path[2] if len(path) == 3 else ''
    return resource_name, resource_id