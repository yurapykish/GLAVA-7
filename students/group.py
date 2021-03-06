# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
#Student model
class Group (models.Model):
        
	class Meta(object):
  	    verbose_name=u'Групи'
      	    verbose_name_plural=u'Групи'

	title = models.CharField(
	    max_length = 256,
	    blank = False,
            verbose_name = u'Назва ГРУПИ')
	leader = models.OneToOneField('Student', verbose_name=u'Староста',
            max_length = 256,
            blank=True,
	    null=True,
	    on_delete=models.SET_NULL)
	notes = models.TextField(
	    blank=True,
	    verbose_name=u'Додаткові нотатки')
	
	def __unicode__(self):
	    if self.leader:

	      return u'%s(%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
	    else:
	      return u"%s" % (self.title,)

