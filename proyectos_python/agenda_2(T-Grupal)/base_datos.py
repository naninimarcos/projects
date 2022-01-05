"------ importaciones de modulos --------------"

from peewee import *
import datetime

"------------- clases -------------------------"

try:
    db = SqliteDatabase('nivel_avanzado.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class Noticia(BaseModel):
        titulo = CharField(unique=True)
        descripcion = TextField()
        fecha = DateTimeField(default=datetime.datetime.now)
        estado_de_publicacion = BooleanField(default=True)
    db.connect()
    db.create_tables([Noticia])

except:
    print("mmmm")
