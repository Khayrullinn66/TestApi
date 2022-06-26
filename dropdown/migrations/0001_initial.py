# Generated by Django 4.0.5 on 2022-06-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_good', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField(unique=True)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subcat', models.CharField(max_length=250)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.category', verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.category', verbose_name='cat')),
                ('name_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.good', verbose_name='good')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.order', verbose_name='order')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.subcategory', verbose_name='subcat')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='subcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.subcategory', verbose_name='subcategory'),
        ),
        migrations.CreateModel(
            name='AllowedCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.category')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.good')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.subcategory')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
