from typing import ClassVar

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering: ClassVar[list[str]] = ["名称"]
        indexes: ClassVar[list] = [models.Index(fields=["名称"])]
        verbose_name: ClassVar[str] = "类别"
        verbose_name_plural: ClassVar[str] = "类别"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="产品", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="产品/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ClassVar[list[str]] = ["名称"]
        indexes: ClassVar[list] = [
            models.Index(fields=["id", "短标题"]),
            models.Index(fields=["名称"]),
            models.Index(fields=["创建日期"]),
        ]

    def __str__(self):
        return self.name
