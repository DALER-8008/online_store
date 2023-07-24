from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBasedModel(models.Model):
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        counter = 1
        slug = f'{base_slug}-{counter}'

        while self.__class__.objects.filter(slug=slug).exists():
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
