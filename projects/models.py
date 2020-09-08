from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    responsibilities = models.TextField()
    technologies = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/project_imgs/%Y/%m/%d',
                              blank=True)

    class Meta:
        ordering = ['technologies',]

    def __str__(self):
        return self.title + '-' + str(self.technologies)