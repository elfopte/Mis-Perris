# Generated by Django 2.1.2 on 2018-10-26 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nciudad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.CharField(max_length=10)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombreP', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('numeroContacto', models.IntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Denominacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nregion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtipoVivienda', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='postulante',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='tipovivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoVivienda'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
    ]