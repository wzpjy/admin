# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TGoods(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    simple_title = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField()
    unit = models.CharField(max_length=4)
    new_price = models.CharField(max_length=100, blank=True, null=True)
    old_price = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    is_comment = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    check_status = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey('TGoodsType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_goods'


class TGoodsPhoto(models.Model):
    photo_url = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    goods = models.ForeignKey(TGoods, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_goods_photo'


class TGoodsType(models.Model):
    type_name = models.CharField(max_length=100, blank=True, null=True)
    type_desc = models.CharField(max_length=200, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    del_time = models.DateTimeField(blank=True, null=True)
    pid = models.ForeignKey('self', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_goods_type'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
