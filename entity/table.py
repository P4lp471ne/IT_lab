from peewee import Model, TextField, ForeignKeyField, IntegerField

from database import db
from entity.database import Database


class Table(Model):
    id: int = IntegerField()
    name: str = TextField()
    database = ForeignKeyField(Database)

    class Meta:
        database = db
        db_table = 'column'
