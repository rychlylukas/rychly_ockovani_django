# Generated by Django 3.2 on 2021-04-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ockovani', '0003_ockovani'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ockovani',
            name='datum_druhe_ockovani',
            field=models.DateField(blank=True, null=True, verbose_name='Datum druhého očkování - dle počtu dávek vakcíny'),
        ),
        migrations.AlterField(
            model_name='ockovani',
            name='datum_narozeni',
            field=models.DateField(verbose_name='Datum narození'),
        ),
        migrations.AlterField(
            model_name='ockovani',
            name='datum_prvni_ockovani',
            field=models.DateField(verbose_name='Datum prvního očkování'),
        ),
    ]