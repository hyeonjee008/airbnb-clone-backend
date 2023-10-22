# Generated by Django 4.2.6 on 2023-10-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('experiences', '0002_remove_perk_detail_perk_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]