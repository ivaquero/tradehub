from typing import ClassVar

from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["名称", "短标题"]
    prepopulated_fields: ClassVar[dict] = {"短标题": ("名称",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = [
        "名称",
        "短标题",
        "价格",
        "有货",
        "创建日期",
        "更新日期",
    ]
    list_filter: ClassVar[list[str]] = ["有货", "创建日期", "更新日期"]
    list_editable: ClassVar[list[str]] = ["价格", "有货"]
    prepopulated_fields: ClassVar[dict] = {"短标题": ("名称",)}
