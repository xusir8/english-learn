# Generated by Django 5.2.4 on 2025-07-17 12:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictation', '0001_initial'),
        ('vocabulary', '0002_reviewplan_wordlearningrecord'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictationrecord',
            options={'verbose_name': '听写记录', 'verbose_name_plural': '听写记录'},
        ),
        migrations.AlterUniqueTogether(
            name='userprogress',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='dictationrecord',
            name='attempt_count',
        ),
        migrations.AddField(
            model_name='dictationrecord',
            name='learning_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vocabulary.wordlearningrecord', verbose_name='学习记录'),
        ),
        migrations.AddField(
            model_name='dictationsession',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='dictationrecord',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='是否正确'),
        ),
        migrations.AlterField(
            model_name='dictationrecord',
            name='time_taken',
            field=models.IntegerField(default=0, verbose_name='用时(秒)'),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='last_practiced',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后练习时间'),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='mastery_level',
            field=models.IntegerField(default=0, verbose_name='掌握程度'),
        ),
    ]
