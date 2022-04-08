# Generated by Django 4.0.3 on 2022-04-08 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_airline_name_airlinecomplaint_airline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fare',
            old_name='tickets',
            new_name='tickets_quantity',
        ),
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/'),
        ),
        migrations.AddField(
            model_name='stay',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stay_images/'),
        ),
        migrations.AddField(
            model_name='stay',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='stay_images/'),
        ),
        migrations.AlterField(
            model_name='airlineadmin',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='airline_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='airlinecomplaint',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='airline_complaints', to='api.airlineadmin'),
        ),
        migrations.AlterField(
            model_name='airlinecomplaint',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_complaints', to='api.airline'),
        ),
        migrations.AlterField(
            model_name='airlinecomplaint',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_complaints', to='api.passenger'),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airplanes', to='api.airline'),
        ),
        migrations.AlterField(
            model_name='airportadmin',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='airport_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='airportcomplaint',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='airport_complaints', to='api.airportadmin'),
        ),
        migrations.AlterField(
            model_name='airportcomplaint',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_complaints', to='api.passenger'),
        ),
        migrations.AlterField(
            model_name='company',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='api.airportadmin'),
        ),
        migrations.AlterField(
            model_name='fare',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fares', to='api.flight'),
        ),
        migrations.AlterField(
            model_name='fare',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flights', to='api.destination'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flights', to='api.airplane'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='api.company'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stay',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stays', to='api.hotel'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='stay',
            name='transac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stays', to='api.transaction'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='api.fare'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='api.passenger'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.company'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.passenger'),
        ),
    ]