from pony.orm import (
    Database,
    Required,
    Set
)

db = Database()


class Event(db.Entity):
    categories = Set('Category')
    cost = Required(int)
    what = Required(str)
    where = Required(str)


class Category(db.Entity):
    name = Required(str)
    events = Set(Event)
