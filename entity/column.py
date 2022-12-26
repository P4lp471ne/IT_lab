from peewee import Model, TextField, IntegerField, ForeignKeyField
from database import db
from entity.table import Table


class EnumField(IntegerField):
    def __init__(self, choices, *args, **kwargs):
        self.to_db = {v: k for k, v in choices}
        self.from_db = {k: v for k, v in choices}
        super(IntegerField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        return self.to_db[value]

    def python_value(self, value):
        return self.from_db[value]


class Column(Model):
    name = TextField()
    type = TextField()
    table = ForeignKeyField(Table)

    class Meta:
        database = db
        db_table = 'column'
