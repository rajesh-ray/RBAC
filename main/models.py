# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)


class ActionType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'action_types'

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)


class Resource(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'resources'

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)


class Role(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'roles'

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)


class UserRole(models.Model):
    user = models.ForeignKey(to='User', related_name='user_of_user_roles')
    role = models.ForeignKey(to='Role', related_name='role_of_user_roles')

    class Meta:
        db_table = 'user_roles'

    def __unicode__(self):
        return '%s - %s - %s' % (self.id, self.user, self.role)


class ResourceActionTypeRole(models.Model):
    resource = models.ForeignKey(to='Resource', related_name='resource_of_resource_action_type_roles')
    action_type = models.ForeignKey(to='ActionType', related_name='action_type_of_resource_action_type_roles')
    role = models.ForeignKey(to='Role', related_name='role_of_resource_action_type_roles')

    class Meta:
        db_table = 'role_resource_action_types'

    def __unicode__(self):
        return '%s - %s - %s - %s' % (self.id, self.role, self.resource, self.action_type)
