import datetime
from pony.orm import (
    Database,
    Required,
    Optional,
    Set
)

db = Database()


class Event(db.Entity):
    categories = Set('Category')
    what = Required(str)
    cost = Required(float)
    when = Required(datetime.date)
    where = Required(str)
    pic_rel = Optional('Image')


class Category(db.Entity):
    name = Required(str)
    events = Set(Event)


class Image(db.Entity):
    file_name = Required(str)
    belongs_to = Required(Event)


db.bind(provider='sqlite', filename='wydra.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
