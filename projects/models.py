from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(null=False, blank=False)
    linkedin = models.URLField(null=False, blank=False)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField()
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name