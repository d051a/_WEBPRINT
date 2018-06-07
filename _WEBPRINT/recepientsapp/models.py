from django.db import models
from django.utils.timezone import now

class Address (models.Model):
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

class Recepient_person(models.Model):
    Name = models.CharField('Имя', max_length = 30)
    LastName = models.CharField('Фамилия', max_length = 30)
    Patronymic = models.CharField('Отчество', max_length = 30)
    pub_date = models.DateField('date published', default = now())
    address = models.CharField('Адрес', max_length = 100)
    index = models.CharField('Индекс', max_length = 6, null = True)

    def __str__(self):
        return self.Name + ' ' + self.LastName

class Recepient_legal(models.Model):
    Title = models.CharField('название', max_length = 30)
    ShortTitle = models.CharField('краткое название', max_length = 30, blank = True)
    Receiver = models.CharField('получатель', max_length = 100, blank = True)
    pub_date = models.DateField('date published', default = now())
    address = models.ManyToManyField(Address, )

    def __str__(self):
        return self.Title
