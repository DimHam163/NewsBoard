# Generated by Django 4.2.2 on 2023-07-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_category_options_remove_announcement_cat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='name',
            field=models.CharField(choices=[('tank', 'Танки'), ('healer', 'Хилы'), ('damager', 'ДД'), ('guild_maste', 'Гилдмастеры'), ('quest_giver', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion_master', 'Зельевары'), ('spell_master', 'Мастер заклинанийы')], default='tank', max_length=13),
        ),
    ]
