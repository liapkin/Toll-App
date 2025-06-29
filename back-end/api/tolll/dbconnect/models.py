# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password


class Operator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True)
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # If the password isn't hashed yet (a simple check, e.g., length or a marker),
        # you can hash it before saving:
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name  # Επιστρέφει το πεδίο `name` ως αναπαράσταση του αντικειμένου
    
    class Meta:
        db_table = 'operator'


class Pass(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    charge = models.FloatField(blank=True, null=True)
    tag = models.ForeignKey('Tag', models.CASCADE, blank=True, null=True)
    tollstation = models.ForeignKey('Tollstation', models.DO_NOTHING, db_column='tollStation_id', blank=True, null=True) 

    class Meta:
        db_table = 'pass'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tagref = models.CharField(db_column='tagRef', max_length=200, blank=True, null=True)
    operator = models.ForeignKey(Operator, models.DO_NOTHING, blank=True, null=True) 

    class Meta:
        db_table = 'tag'


class Tollstation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    road = models.CharField(max_length=200, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    price1 = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    price3 = models.FloatField(blank=True, null=True)
    price4 = models.FloatField(blank=True, null=True)
    tollid = models.CharField(max_length=50, blank=True, null=True)
    operator = models.ForeignKey(Operator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'tollstation'
