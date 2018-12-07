from django.db import models


class Bookmark(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
