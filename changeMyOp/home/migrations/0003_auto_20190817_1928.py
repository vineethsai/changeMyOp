# Generated by Django 2.2.4 on 2019-08-18 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dislike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='opinion_comment', to='home.Comment'),
        ),
    ]
