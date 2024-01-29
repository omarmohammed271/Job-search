from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
JOB_TYBE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
# Create your models here.
def image_upload(instance,filename):
    imagename,extension = filename.split('.')
    return f'jobs\{instance.id}.{extension}'
class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_type =  models.CharField(max_length=15,choices=JOB_TYBE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Apply(models.Model):
   
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)   
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField( upload_to='apply/')
    cover_letter = models.TextField()
    published = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



    

    