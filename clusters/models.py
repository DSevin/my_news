from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    url = models.URLField()
    content = models.TextField(blank=False, null=False)
    cluster = models.IntegerField()

    def __str__(self):
        return self.title
