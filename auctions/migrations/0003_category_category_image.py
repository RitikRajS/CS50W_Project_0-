# Generated by Django 5.1 on 2024-11-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_auction_bid_comment_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.URLField(blank=True, max_length=5000),
        ),
    ]
