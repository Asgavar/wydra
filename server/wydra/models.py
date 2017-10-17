from pony.orm import *

db = Database()

class Event(db.Entity):
    what     = Required(str)
    where    = Required(str)
    cost     = Required(int)
    category = Required('Category')


class Category(db.Entity):
    name   = Required(str)
    events = Set(Event)
