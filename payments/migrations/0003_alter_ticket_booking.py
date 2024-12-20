# Generated by Django 4.2.13 on 2024-12-02 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_booking_date'),
        ('payments', '0002_remove_ticket_qr_code_ticket_total_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='booking.booking'),
        ),
    ]
