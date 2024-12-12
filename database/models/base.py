from database import db
from peewee import Model, AutoField, DateTimeField
from datetime import datetime


class BaseModel(Model):
    """
    Базовая модель с автоматическим заполнением поля ID и сохранением времени создания, изменения
    """
    ID = AutoField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
