from django.db import models


class Category(models.Model):
    # Id = models.IntegerField(primary_key=True, unique=True, verbose_name="کلید اصلی")
    name = models.CharField(max_length=30, verbose_name="دسته بندی")

    def __str__(self):
        return f"{self.name}"


class SubCategory(models.Model):
    # Id = models.IntegerField(primary_key=True, unique=True, verbose_name="کلید فرعی")
    parent = models.ForeignKey(Category, verbose_name="ردسته بندی", on_delete=models.CASCADE)
    # parent = models.ManyToManyField(Category, verbose_name="دسته بندی", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="زیردسته بندی")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    # Id = models.IntegerField(primary_key=True, unique=True, verbose_name="شماره محصول")
    name = models.CharField(max_length=30, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")
    description = models.TextField(max_length=300, verbose_name="توضیحات")
    image = models.ImageField(upload_to="Products/", verbose_name="تصویر")
    # category = models.ManyToManyRel(SubCategory, verbose_name="دسته بندی")
    category = models.ForeignKey(SubCategory, verbose_name="دسته بندی", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
