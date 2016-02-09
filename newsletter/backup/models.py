# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import User

# class Subscriber(models.Model):
#     user = models.ForeignKey(User)
#     email = models.EmailField()

#     def __str__(self):
#         return "User %s" % (self.user.username, )

#     @models.permalink
#     def get_absolute_url(self):
#         return ('subscriber', None, {'object_id' : self.id})

#     class Meta:
#         ordering = [ "id" ]

# class Newsletter(models.Model):
#     name = models.CharField(max_length=80)
#     subscribers = models.ManyToManyField('Subscriber')
#     # .... Other stuff

#     def __str__(self):
#         return "Newsletter %s" % (self.name, )

#     @models.permalink
#     def get_absolute_url(self):
#         return ('newsletter', None, {'object_id' : self.id})

#     class Meta:
#         ordering = [ "id" ]