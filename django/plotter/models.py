from django.db import models

# Create your models here.

class Experiments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'experiments'
        
    def __str__(self):
        return self.name


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