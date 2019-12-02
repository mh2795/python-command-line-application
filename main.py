import sys
from peewee import PostgresqlDatabase, Model, CharField, BigIntegerField

db = PostgresqlDatabase('contacts', user='mustafahassan', password='',
                        host='localhost', port=5432)
db.connect()


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    phone = BigIntegerField()

    class Meta:  # magic
        database = db  # This model uses the "contacts.db" database.


db.create_tables([Contact])

