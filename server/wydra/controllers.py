import cgi
import datetime

import pystache
from pony import orm
from models import Event

"""
Controllers here are basically black boxes which take HTTP request body
and (hypotheticaly) resource_id* as input and provide an output which is
then sent to client.
*actually it's the other way around, but sounds better this way
"""


@orm.db_session
def get_all_events():
    event_list = orm.select(e for e in Event)
    with open('/home/asgavar/wydra/server/wydra/template.mustache') as t:
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


@orm.db_session
def post_event(id, request_body):
    vals = cgi.parse_qs(request_body)
    vals = {key: value[0] for key, value in vals.items()}
    e = Event(
        what=vals[b'what'].decode('utf-8'), cost=float(vals[b'cost']),
        when=datetime.datetime.strptime(vals[b'when'][:10].decode('utf-8'), '%Y-%m-%d'),
        where=vals[b'where'].decode('utf-8')
    )
    return b'received'


def delete_event(id, request_body):
    pass
