from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.conf import settings
import re
from django.db.models import Q
from my_pystagram.validators import jpeg_validator
from django.db.models.signals import pre_save
from my_pystagram.image import receiver_with_image_field
from my_pystagram.file import random_name_with_file_field

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# def validate_hexstring(value):
#     if not re.match(r'^[0-9a-fA-F]+$', value):
#         raise ValidationError("hexstring 이 아니오.")


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    uuid = models.UUIDField(default=uuid4, editable=False, db_index=True)
    category = models.ForeignKey(Category)
    #구글 지도 위젯 위경도 데이터
    photo = models.ImageField(blank=True, null=True, validators=[jpeg_validator], upload_to=random_name_with_file_field)
    lnglat = models.CharField(max_length=100, blank=True, null=True)
    # title = models.CharField(max_length=100, db_index=True,validators=[validate_hexstring])
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    origin_url = models.URLField(blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('blog:detail', args=[self.uuid.hex])
        return reverse('blog:detail', args=[self.pk])

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]

    @classmethod
    def timeline(cls, from_user):
        following_users = [follow.to_user_id for follow in from_user.following_set.all()]
        return cls.objects.filter(Q(author=from_user) | Q(author__in=following_users))

receiver = receiver_with_image_field('photo', 1024)
pre_save.connect(receiver, sender=Post)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Photograph(models.Model):
    #image_url = models.URLField()
    image_file = models.ImageField(upload_to='%Y/%m/%d/')
    description = models.TextField(null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


