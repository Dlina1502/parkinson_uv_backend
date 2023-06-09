# Generated by Django 4.1.2 on 2023-04-25 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game_settings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('time_seconds', models.IntegerField()),
                ('specifications', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parkinson_phase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phase', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('id_type', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('cell', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('id_type', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('cell', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=3)),
                ('is_active', models.BooleanField()),
                ('id_parkinson_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.parkinson_phase')),
                ('id_therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.patient')),
                ('id_therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='Game_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.JSONField()),
                ('id_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.game')),
                ('id_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.list')),
                ('id_setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.game_settings')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.game_type'),
        ),
    ]
