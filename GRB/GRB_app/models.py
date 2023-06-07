# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BookCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'book_category'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    languages = models.CharField(max_length=50)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    publisher = models.ForeignKey('Publishers', models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'books'


class Publishers(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'publishers'


class Stores(models.Model):
    store_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city_id = models.IntegerField()
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'stores'