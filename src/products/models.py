from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Boolean, MetaData

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("updated_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True),
)


# class Product(Model):
#     """ Модель товара """
#
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=100, verbose_name='наименование товара')
#     price = fields.IntField(verbose_name='стоимость товара')
#     created_at = fields.DatetimeField(auto_now_add=True, verbose_name='дата создания')
#     updated_at = fields.DatetimeField(auto_now=True, verbose_name='дата изменения')
#     is_active = fields.BooleanField(default=True, verbose_name='признак активности')
#
#     def __str__(self):
#         return f'{self.name}'
