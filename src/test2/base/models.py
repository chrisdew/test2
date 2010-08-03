from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    info = models.C

    class Meta:
        db_table = u'user_profile'

