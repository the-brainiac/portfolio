from django.db import models

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Project(models.Model):
    project_name  = models.CharField(max_length=200)
    about         = models.CharField(max_length=200, null=True, blank=True)
    thumbnail     = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    active        = models.BooleanField(default=False)
    featured      = models.BooleanField(default=False)
    tags          = models.ManyToManyField(Tag, null=True, blank=True)
    redirect_link = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.project_name
