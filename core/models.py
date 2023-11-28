from django.db import models
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() 
    startYear = models.IntegerField()
    endYear = models.IntegerField() # TODO: If endYear is null display PRESENT
    link = models.CharField(max_length=255)
    tags = models.JSONField('tags')

    class Meta:
        ordering = ('startYear',) # Order list based on start year

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() 
    link = models.CharField(max_length=500)
    tags = models.JSONField('tags')

    class Meta:
        ordering = ('title',) # Order list alphabetly based on the job title

    def __str__(self):
        return self.title