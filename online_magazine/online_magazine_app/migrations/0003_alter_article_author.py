# Generated by Django 4.2.7 on 2023-11-10 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_magazine_app', '0002_alter_article_id_alter_category_id_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_magazine_app.userdetails'),
        ),
    ]