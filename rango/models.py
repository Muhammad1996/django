from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

length_value = 128

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=length_value, unique=True)
    likes= models.IntegerField(default=0)
    views= models.IntegerField(default=0)
    slug= models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name

    def __unicode__(self):  # For Python 2, use __unicode__ too
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=length_value)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title

    def __unicode__(self):  # For Python 2, use __unicode__ too
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.user.username

    def __unicode__(self):  # For Python 2, use __unicode__ too
        return self.user.username