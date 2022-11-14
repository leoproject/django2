# Generated by Django 4.1.3 on 2022-11-14 13:08

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateField(auto_now_add=True, verbose_name="Create Date"),
                ),
                (
                    "modificated",
                    models.DateField(auto_now=True, verbose_name="Update Date"),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Active?")),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Price"
                    ),
                ),
                ("stock", models.IntegerField(verbose_name="Stock")),
                (
                    "image",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        upload_to="products",
                        variations={"thumb": (124, 124)},
                        verbose_name="Image",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, editable=False, max_length=100, verbose_name="Slug"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
