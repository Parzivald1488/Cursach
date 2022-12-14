from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField('Название', max_length=50)

    def get_absolute_url(self):
        return reverse('subject')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)

    def getFullName(self):
        return f'{self.surname} {self.name} {self.patronymic}'
  
    def getShortName(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'

    def get_absolute_url(self):
        return reverse('teacher')

    def __str__(self):
        return self.getShortName()


class Speciality(models.Model):
    title = models.CharField('Название', max_length=50)
    abbreviation = models.CharField('Аббревиатура', max_length=8)
    code = models.CharField('Код специальности', max_length=15, unique=True)

    def get_absolute_url(self):
        return reverse('speciality')

    def __str__(self):
        return f'{self.abbreviation}: {self.title}'


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    course = models.IntegerField('Курс')
    number = models.CharField('Номер группы', max_length=10)

    def getName(self):
        return f'{self.speciality.abbreviation}-{self.course}{self.number}'

    def get_absolute_url(self):
        return reverse('group')

    def __str__(self):
        return self.getName()


class Time(models.Model):
    name = models.CharField('Название', max_length=15)
    start = models.TimeField('Начало')
    end = models.TimeField('Конец')

    def get_absolute_url(self):
        return reverse('time')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    data = models.DateField('Дата')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    cabinet = models.CharField('Кабинет', max_length=7)

    def get_absolute_url(self):
        return reverse('lesson')

    def __str__(self):
        return f'{self.data}: {self.subject.name}, {self.group.getName()}, {self.teacher.getShortName()}'