# Generated by Django 4.2.7 on 2024-01-31 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basemodel",
                    ),
                ),
                ("name", models.CharField(max_length=55)),
            ],
            bases=("main.basemodel",),
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basemodel",
                    ),
                ),
                ("name", models.CharField(max_length=55)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone_number", models.CharField(max_length=55)),
                ("content", models.TextField(null=True)),
            ],
            bases=("main.basemodel",),
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basemodel",
                    ),
                ),
                ("name", models.CharField(max_length=55)),
            ],
            bases=("main.basemodel",),
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basemodel",
                    ),
                ),
                (
                    "complaint",
                    models.CharField(
                        choices=[
                            ("Noo'rin savol/izoh", "No"),
                            ("Insonning sha'niga teguvchi gaplar", "In"),
                            ("Boshqalarga nisbatan so'kish", "Bo"),
                            ("Terrorizmga da'vat", "Te"),
                            ("Tushunarsiz va umuman kerak bo'lmagan izoh", "Tu"),
                        ],
                        default="Noo'rin savol/izoh",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("content", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            bases=("main.basemodel",),
        ),
    ]
