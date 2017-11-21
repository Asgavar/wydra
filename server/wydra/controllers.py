import pystache
from pony import orm
from models import *

"""
Controllers here are basically black boxes which take HTTP request body
and (hypotheticaly) resource_id* as input and provide an output which is
then sent to client.
*actually it's the other way around, but sounds better this way
"""


@orm.db_session
def get_all_events():
    event_list = orm.select(e for e in Event)
    with open('template.mustache') as t:
        ret = pystache.render(t.read(), event_list=event_list)
    return ret.encode()


def get_event(id, request_body):
    """
    Receives desired event's id (or None) and returns appropriately filled
    HTML template.
    """
    if not id:
        return get_all_events()
    return bytes(f'event no. {id}', 'utf-8')


def post_event(id, request_body):
    pass


def delete_event(id, request_body):
    pass
