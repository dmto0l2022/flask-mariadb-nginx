# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
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
    action_flag = models.PositiveSmallIntegerField()
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


class DjangoPlotlyDashDashapp(models.Model):
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.IntegerField()
    stateless_app = models.ForeignKey('DjangoPlotlyDashStatelessapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experiments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiments'


class LimitDisplays(models.Model):
    limit_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_displays'


class LimitOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    limit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_ownerships'


class Limits(models.Model):
    spin_dependency = models.CharField(max_length=255, blank=True, null=True)
    result_type = models.CharField(max_length=255, blank=True, null=True)
    measurement_type = models.CharField(max_length=60, blank=True, null=True)
    nomhash = models.TextField(blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    x_rescale = models.CharField(max_length=255, blank=True, null=True)
    y_rescale = models.CharField(max_length=255, blank=True, null=True)
    default_color = models.CharField(max_length=255, blank=True, null=True)
    default_style = models.CharField(max_length=255, blank=True, null=True)
    data_values = models.TextField(blank=True, null=True)
    data_label = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    data_comment = models.CharField(max_length=255, blank=True, null=True)
    data_reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    experiment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    date_of_announcement = models.DateField(blank=True, null=True)
    public = models.IntegerField(blank=True, null=True)
    official = models.IntegerField(blank=True, null=True)
    date_official = models.DateField(blank=True, null=True)
    greatest_hit = models.IntegerField(blank=True, null=True)
    date_of_run_start = models.DateField(blank=True, null=True)
    date_of_run_end = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limits'


class MyUsers(models.Model):
    login = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    crypted_password = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    salt = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    remember_token_expires_at = models.DateTimeField(blank=True, null=True)
    reset_password_code = models.CharField(max_length=255, blank=True, null=True)
    reset_password_code_until = models.DateTimeField(blank=True, null=True)
    activation_code = models.CharField(max_length=255, blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_users'


class PlotOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plot_ownerships'


class Plots(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    x_min = models.CharField(max_length=255, blank=True, null=True)
    x_max = models.CharField(max_length=255, blank=True, null=True)
    y_min = models.CharField(max_length=255, blank=True, null=True)
    y_max = models.CharField(max_length=255, blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    plot_png = models.TextField(blank=True, null=True)
    legend_png = models.TextField(blank=True, null=True)
    plot_eps = models.TextField(blank=True, null=True)
    legend_eps = models.TextField(blank=True, null=True)
    no_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plots'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SimpleCaptchaData(models.Model):
    key = models.CharField(max_length=40, blank=True, null=True)
    value = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simple_captcha_data'


class Users(models.Model):
    login = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    crypted_password = models.CharField(max_length=40, blank=True, null=True)
    salt = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    remember_token_expires_at = models.DateTimeField(blank=True, null=True)
    reset_password_code = models.CharField(max_length=255, blank=True, null=True)
    reset_password_code_until = models.DateTimeField(blank=True, null=True)
    activation_code = models.CharField(max_length=255, blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
