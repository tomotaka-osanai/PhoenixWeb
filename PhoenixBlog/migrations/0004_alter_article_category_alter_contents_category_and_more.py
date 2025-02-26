# Generated by Django 4.1.7 on 2023-04-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoenixBlog', '0003_contents_article_is_published_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contents',
            name='category',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
