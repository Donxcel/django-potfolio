from django.db import models
import uuid
# Create your models here.
# Create your models here.

# creating a model to easily add projects in our database
class Project(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    intro = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, db_index=True)
    image_description = models.ImageField(null=True, blank = True, default='default.jpeg')
    def __str__(self):
        return self.title
    

class Info(models.Model):
    # user_id = models.UUIDField(
    #     default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    email_link = models.URLField(blank=True)
    title_description = models.TextField(blank=True, null=True)
    full_description  = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100,blank=True)
    quarter = models.CharField(max_length=100,blank=True)
    region = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    cv_link = models.URLField(blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image_profile = models.ImageField(null=True, blank = True, default='default.jpeg')

    def __str__(self):
        return self.first_name