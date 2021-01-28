from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),  # (storeDatabase,userView)
    ('Part Time', 'Part Time'),
)


class Job(models.Model):
    # location
    owner = models.ForeignKey(User, related_name='owner_job',
                              on_delete=models.CASCADE)  # user here by django for admin or user
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    published_at = models.DateTimeField(auto_now=True)  # updated_at
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs/')
    slug = models.SlugField(blank=True, null=True)

    # overwrite save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # import
        super(Job, self).save(*args, **kwargs)

    def __str__(self):  # for name job in admin panel 
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)

    # created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
