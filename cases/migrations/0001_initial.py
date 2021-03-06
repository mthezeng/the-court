# Generated by Django 3.2.7 on 2021-09-23 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Justice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_chief_justice', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_type', models.CharField(choices=[('M', 'Majority'), ('P', 'Plurality'), ('C', 'Concurring'), ('D', 'Dissenting')], default='M', max_length=2)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='cases.justice')),
                ('joined_by', models.ManyToManyField(blank=True, related_name='_cases_opinion_joined_by_+', to='cases.Justice')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('argued_date', models.DateField()),
                ('decided_date', models.DateField()),
                ('citation', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('commentary', models.TextField()),
                ('case_opinions', models.ManyToManyField(to='cases.Opinion')),
            ],
        ),
    ]
