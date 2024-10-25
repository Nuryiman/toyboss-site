from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def get_short_description(self):
        return self.description[:300] + '...'
