from django.db import models
from django.utils.text import slugify

# Create your models here.
class job_post(models.Model):
    title=models.CharField(max_length=200)
    discription=models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        return super(job_post, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} with Description {self.discription}"

