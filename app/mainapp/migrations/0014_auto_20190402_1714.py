# Generated by Django 2.0.8 on 2019-04-02 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20190402_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.Template', verbose_name='Шаблон'),
        ),
    ]
