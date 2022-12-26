from peewee import Model, IntegerField, TextField

from database import db


class Database(Model):
    id: int = IntegerField()
    name: str = TextField()

    class Meta:
        database = db
        db_table = 'column'
