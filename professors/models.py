from django.db import models


class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    image_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "testimonials_professor"

    def __str__(self):
        return self.name
