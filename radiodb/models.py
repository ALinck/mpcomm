# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class RadioChoices(models.Model):
    CURRENT_CHOICES = [
        ('YES', 'YES'),
        ('NO', 'NO')
    ]

    TYPE_CHOICES = [
        ('PORTABLE', 'PORTABLE'),
        ('MOBILE', 'MOBILE'),
        ('CONSOLETTE', 'CONSOLETTE'),
        ('MINI-BASE', 'MINI-BASE'),
        ('AIRBAND', 'AIRBAND'),
        ('OTHER', 'OTHER')
    ]

    MODEL_CHOICES = [
        ('XTS2500', 'XTS2500'),
        ('XTS5000 M1', 'XTS5000 M1'),
        ('XTS5000 M2', 'XTS5000 M2'),
        ('XTS5000 M3', 'XTS5000 M3'),
        ('XTL2500', 'XTL2500'),
        ('XTL5000 W', 'XTL5000 W'),
        ('XTL5000 O', 'XTL5000 O'),
        ('APX6000', 'APX6000'),
        ('APX6500', 'APX6500'),
        ('APX7000', 'APX7000'),
        ('APX7500', 'APX7500'),
        ('APX8000', 'APX8000'),
        ('IC-A200', 'IC-A200'),
        ('IC-A210', 'IC-A210'),
        ('IC-A110', 'IC-A110')
    ]

    STATUS_CHOICES = [
        ('NORMAL', 'NORMAL'),
        ('NEEDS SVC', 'NEEDS SVC'),
        ('NEEDS PROG', 'NEEDS PROG'),
        ('OUT FOR SVC', 'OUT FOR SVC'),
        ('NOT IN USE', 'NOT IN USE'),
        ('TEMP IN USE', 'TEMP IN USE'),
        ('SHOP', 'SHOP'),
        ('IN SHOP/NP', 'IN SHOP/NP'),
        ('NEEDS FLASH', 'NEEDS FLASH')
    ]

    OPERATION_CHOICES = [
        ('REPROGRAM', 'REPROGRAM'),
        ('FLASH UPGRADE', 'FLASH UPGRADE'),
        ('CHANGE ID', 'CHANGE ID'),
        ('SERVICE', 'SERVICE'),
        ('STATUS CHECK', 'STATUS CHECK'),
        ('INSTALLED', 'INSTALLED'),
        ('CLEANED', 'CLEANED')
    ]

    CODEPLUG_CHOICES = [
        ('ARFF', 'ARFF'),
        ('CAP PGMS', 'CAP PGMS'),
        ('CONSTRUCTION', 'CONSTRUCTION'),
        ('FAC MGMT', 'FAC MGMT'),
        ('FAC WRKR', 'FAC WRKR'),
        ('HANSCOM', 'HANSCOM'),
        ('IT', 'IT'),
        ('MRTM MGMT', 'MARITIME MGMT'),
        ('MRTM WRKR', 'MARITIME WRKR'),
        ('MPA POLICE', 'MPA POLICE'),
        ('OPS', 'OPS'),
        ('TRANSPORT', 'TRANSPORT'),
        ('TSA', 'TSA'),
        ('MSP', 'MSP'),
        ('NONE', 'NONE'),
        ('T16 OPS', 'T16 OPS'),
        ('ORH', 'ORH'),
        ('ORH PS', 'ORH PUB SAFE'),
        ('CUSTOM', 'CUSTOM')
    ]


class MassportMaster(models.Model):
    unit_id = models.IntegerField(db_column='UNIT ID', blank=True, null=True)
    serial_number = models.TextField(db_column='SERIAL NUMBER', blank=True, null=True)
    model = models.TextField(db_column='MODEL', choices=RadioChoices.MODEL_CHOICES, blank=True, null=True)
    model_number = models.TextField(db_column='MODEL NUMBER', blank=True, null=True)
    type = models.TextField(db_column='TYPE', choices=RadioChoices.TYPE_CHOICES, blank=True, null=True)
    flash = models.TextField(db_column='FLASH', blank=True, null=True)
    flashport = models.TextField(db_column='FLASHPORT', blank=True, null=True)
    current = models.TextField(db_column='CURRENT', choices=RadioChoices.CURRENT_CHOICES, blank=True, null=True)
    status = models.TextField(db_column='STATUS', choices=RadioChoices.STATUS_CHOICES, blank=True, null=True)
    issued_to = models.TextField(db_column='ISSUED TO', blank=True, null=True)
    last_prog = models.TextField(db_column='LAST PROG', blank=True, null=True)
    codeplug = models.TextField(db_column='CODEPLUG', choices=RadioChoices.CODEPLUG_CHOICES, blank=True, null=True)
    operation = models.TextField(db_column='OPERATION', blank=True, null=True)
    date = models.TextField(db_column='DATE', blank=True, null=True)
    notes = models.TextField(db_column='NOTES', blank=True, null=True)
    id = models.IntegerField(db_column='id', primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'massport master'


class RadioForm(ModelForm):
    class Meta:
        model = MassportMaster
        fields = ['unit_id',
                  'serial_number',
                  'model',
                  'model_number',
                  'type',
                  'flash',
                  'flashport',
                  'current',
                  'status',
                  'issued_to',
                  'last_prog',
                  'codeplug',
                  'operation',
                  'date',
                  'notes',
                  ]
