from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=50)
    

class Poi(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'poi'
