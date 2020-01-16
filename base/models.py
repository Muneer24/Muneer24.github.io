from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save,pre_save
from djmoney.models.fields import MoneyField
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

class Product(models.Model):
    image = models.FileField(upload_to="Products", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Product'  
        verbose_name_plural = 'Products'















