from django.db import models
from django.urls import reverse


class Category(models.Model):
    # ...
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    # ...
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
