# Generated by Django 5.1.2 on 2024-11-12 04:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('payment_method', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(upload_to='ticket_qr_Codes')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='booking.booking')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='booking.seat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
