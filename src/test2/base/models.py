from django.db import models

class UserProfile(models.Model):
    info = models.Char

    class Meta:
        db_table = u'user_profile'

