# Generated by Django 4.2.7 on 2023-11-10 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import watchapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchapp', '0005_product_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cards',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=watchapp.models.getproductimage),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchapp.product_cards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
