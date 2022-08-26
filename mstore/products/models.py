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
    name = models.CharField(max_length=30, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")
    description = models.TextField(max_length=300, verbose_name="توضیحات")
    image = models.ImageField(upload_to="Products/", verbose_name="تصویر")
    # category = models.ManyToManyRel(SubCategory, verbose_name="دسته بندی")
    category = models.ForeignKey(SubCategory, verbose_name="دسته بندی", on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False, verbose_name="حذف شده")

    def __str__(self):
        return f"{self.name}"


# from django_resized import ResizedImageField
# post_image = ResizedImageField(size=[500, 300], upload_to=get_image_path, blank=True, null=True)

# ----------------------------------------------------------------------------------------------

# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
#
# def upload_image_path(instance, filename):
#     par = MAgahi.objects.filter(nevisande=instance.nevisande)
#     parl = len(par)+1
#     name, ext = get_filename_ext(filename)
#     final_name = f"{parl}-{instance.nevisande}{ext}"
#     return f"{instance.nevisande}/{final_name}"
#
#
# class MAgahi(models.Model):
#     nevisande = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
#     onvan = models.CharField(max_length=50, default='title')
#     aks = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس')
#     txt = models.TextField(max_length=200, blank=True, null=True)
#     def str(self):
#         return self.onvan
