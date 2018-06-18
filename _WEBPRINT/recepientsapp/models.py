from django.db import models
from django.utils.timezone import now

class Address(models.Model):
    LEGAL = 'LG'
    POSTAL = 'PL'
    FACT = 'FT'
    address_type = (
    (LEGAL, 'Юридический'),
    (FACT, 'Фактический'),
    (POSTAL, 'Почтовый'),
    )
    address = models.CharField('Адрес', max_length = 100)
    city = models.CharField('Город', max_length = 20)
    index = models.CharField('Индекс', max_length = 6)
    choices = models.CharField('Тип адреса', max_length=2, choices = address_type, default=FACT)

    def __str__(self):
        return self.city + ' ' + self.address

class Recepient(models.Model):
    title = models.CharField('ФИО или название организации', max_length = 30)
    pub_date = models.DateField('Дата публикации', auto_now_add = True)
    address = models.CharField('Адрес', max_length = 100)
    postcode = models.CharField('Индекс', max_length = 6, null = True)
    class Meta:
        ordering = ['title']
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
    def __str__(self):
        return self.title

class Envelop_format (models.Model):
    def __str__(self):
        return self.env_form_title
    env_form_title = models.CharField('Формат конверта', max_length = 30)
    class Meta:
        ordering = ['pk']
        verbose_name = 'Формат конверта'
        verbose_name_plural = 'Форматы конвертов'



class Envelop(models.Model):
    env_title = models.CharField('Название конверта', max_length = 30)
    envelop_format = models.ForeignKey(Envelop_format)
    envelop_template = models.FileField('Шаблон конверта')
    class Meta:
        ordering = ['-pk']
        verbose_name = 'Конверт'
        verbose_name_plural = 'Конверты'
    def __str__(self):
        return self.env_title
