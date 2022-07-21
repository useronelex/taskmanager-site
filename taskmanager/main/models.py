from django.db import models


class Task(models.Model):
    title = models.CharField('Назава', max_length=50)
    text = models.TextField('Опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Всі завдання'
