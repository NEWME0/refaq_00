from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Scope(models.Model):
    title = models.CharField(max_length=20)
    group = models.ForeignKey(Group, related_name='scope_group', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='scope_users')
