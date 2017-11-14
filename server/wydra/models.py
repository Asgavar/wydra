from pony.orm import (
    Database,
    Required,
    Optional,
    Set
)

db = Database()


class Event(db.Entity):
    categories = Set('Category')
    cost = Required(int)
    what = Required(str)
    where = Optional(str)
    pic_rel = Optional('Image')


class Category(db.Entity):
    name = Required(str)
    events = Set(Event)


class Image(db.Entity):
    file_name = Required(str)
    belongs_to = Required(Event)
