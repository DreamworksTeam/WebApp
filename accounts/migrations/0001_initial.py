# Generated by Django 2.2.1 on 2019-05-11 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('contact_address', models.TextField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12)),
                ('place_of_birth', models.TextField()),
                ('Dob', models.DateField(default=django.utils.timezone.now)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=30)),
                ('course', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=11)),
                ('academic_qualifications', models.CharField(choices=[('O Level', 'O Level'), ('BSC', 'BSC'), ('MSC', 'MSC'), ('PHD', 'PHD')], max_length=20)),
                ('session', models.CharField(choices=[('Morning (10am)', 'Morning (10am)'), ('Afternoon (10am)', 'Afternoon (10am)')], max_length=40)),
                ('disability', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('next_of_kin_phone', models.CharField(max_length=11)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
