# Generated by Django 3.1.3 on 2024-01-21 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('book_id', models.CharField(db_index=True, max_length=35)),
                ('title', models.CharField(max_length=250)),
                ('no_of_copies', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='book_management_application.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('member_id', models.CharField(db_index=True, max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationDetails',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_management_application.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_management_application.member')),
            ],
        ),
        migrations.CreateModel(
            name='BookCheckoutDetails',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('fine_paid', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_management_application.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_management_application.member')),
            ],
        ),
    ]
