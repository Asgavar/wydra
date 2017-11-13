"""
Syntax for using this is:

    mapping[<http method>][<resource_name>](resource_id, request_body)

which calls the appropriate controller function.
Both resource_id and request_body can be empty strings.
"""

from controllers import (
    get_event,
    post_event,
    delete_event
)

mapping = {
    'GET': {
        'events': get_event
    },
    'POST': {
        'events': post_event
    },
    'DELETE': {
        'events': delete_event
    }
}
