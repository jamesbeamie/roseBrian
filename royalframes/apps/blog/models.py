from django.db import models

class Blog(models.Model):
    image_path = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    title = models.CharField(db_index=True, max_length=255)
    body = models.CharField(db_index=True, max_length=8055)
    # tags = models.ManyToManyField('articles.Tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_path