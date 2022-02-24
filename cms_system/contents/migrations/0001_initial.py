# Generated by Django 4.0.1 on 2022-02-24 10:18

import contents.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('lastEditDate', models.DateTimeField(auto_now=True)),
                ('is_Accepted', models.BooleanField(default=True)),
                ('contentType', models.CharField(max_length=3, null=True)),
                ('hits', models.DecimalField(decimal_places=0, default=0, max_digits=11, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to=contents.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4'])])),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('themeValue', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail_Theme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
                ('theme_id', models.ForeignKey(db_column='theme_id', on_delete=django.db.models.deletion.CASCADE, related_name='Detail_Theme', to='contents.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Contents_Description',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', tinymce.models.HTMLField()),
                ('width', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('HVType', models.CharField(max_length=10, null=True)),
                ('thumbnailPath', models.CharField(max_length=200, null=True)),
                ('contentFK', models.ForeignKey(blank=True, db_column='contentsFK', null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.contents')),
            ],
        ),
        migrations.AddField(
            model_name='contents',
            name='theme_id',
            field=models.ForeignKey(blank=True, db_column='theme_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='contents.theme'),
        ),
        migrations.AddField(
            model_name='contents',
            name='userFK',
            field=models.ForeignKey(db_column='userFK', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Content_Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents_id', models.ForeignKey(db_column='contents_id', on_delete=django.db.models.deletion.CASCADE, related_name='Content_Like', to='contents.contents')),
                ('userFK', models.ForeignKey(db_column='userFK', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents_id', models.ForeignKey(db_column='contents_id', on_delete=django.db.models.deletion.CASCADE, related_name='Content_Comment', to='contents.contents')),
                ('userFK', models.ForeignKey(db_column='userFK', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
