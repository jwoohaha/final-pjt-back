
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('backdrop_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
