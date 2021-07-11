from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=10, unique=True)
    description = models.TextField(max_length=50)
    category_name = models.CharField(max_length=255)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name
        