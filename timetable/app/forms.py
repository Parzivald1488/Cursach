from django import forms
from django.forms import ModelForm, TextInput, Select, ValidationError
from .models import Group, Teacher, Subject, Speciality, Time, Lesson

class CalendarFilterForm(forms.Form):
    teacher = forms.ChoiceField(
        label='Преподаватель',
        required=False,
        choices=[('','Выберите преподавателя')] + [(x.id, x.getFullName()) for x in Teacher.objects.all()]
    )
    group = forms.ChoiceField(
        label='Группа',
        required=False,
        choices=[('','Выберите группу')] + [(x.id, x.getName()) for x in Group.objects.all()]
    )

# Предмет

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

        widgets = {
            "name" : TextInput(attrs={
                'class' :  'form-control',
                'placeholder': 'Название предмета'
            })
        }

# Учитель

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['surname', 'name', 'patronymic']

        widgets = {
            "surname" : TextInput(attrs={
                'class' :  'form-control',
                'placeholder': 'Фамилия преподавателя'
            }),
            "name" : TextInput(attrs={
                'class' :  'form-control',
                'placeholder': 'Имя преподавателя'
            }),
            "patronymic" : TextInput(attrs={
                'class' :  'form-control',
                'placeholder': 'Отчество преподавателя'
            }),
        }

# Специальность

class SpecialityForm(ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'abbreviation', 'code']

        widgets = {
            "title" : TextInput(attrs={
                'class' :  'form-control',
                
            }),
            "abbreviation" : TextInput(attrs={
                'class' :  'form-control',
                
            }),
            "code" : TextInput(attrs={
                'class' :  'form-control',
                
            }),
        }

# Группа

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['speciality', 'course', 'number']

        widgets = {
             "speciality"  : Select(attrs={
                'class' :   'form-select',
            }),
            "course" : TextInput(attrs={
                'type': 'number', 
                'class' :  'form-control'
            }),
            "number" : TextInput(attrs={
                'class' :  'form-control',
                'placeholder': 'Номер группы'
            }),
        }

# Время

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ['name', 'start', 'end']

        widgets = {
            "name"  : TextInput(attrs= {
                'class' : 'form-control',
                'placeholder': 'Название'
            }),
            "start" : TextInput(attrs={
                'type': 'time', 
                'class' :  'form-control'
            }),
                "end" : TextInput(attrs={
                'type': 'time', 
                'class' :  'form-control'
            }),
        }

# Занятие

class LessonForm(ModelForm):
    def clean(self):
        data = super().clean()
        date = data.get("data")
        time = data.get("time")
        teacher = data.get("teacher")
        group = data.get("group")
        cabinet = data.get("cabinet")

        lessons = Lesson.objects.filter(
            data__year = date.year,
            data__month = date.month,
            data__day = date.day,
            time = time,
        )
        lesson_teacher = lessons.filter(
            teacher = teacher,
        )
        lesson_group = lessons.filter(
            group = group,
        )
        lesson_cabinet = lessons.filter(
            cabinet = cabinet,
        ) 
        
        error = []

        if  (lesson_teacher.count() > 0):
            error.append("У преподавателя уже есть занятие в это время.")

        if  (lesson_group.count() > 0):
            error.append("У группы уже есть занятие в это время.")

        if  (lesson_cabinet.count() > 0):
            error.append("Этот кабинет занят в это время.")

        if (error.__len__() > 0):
            raise ValidationError(error)

        print("WORK!!!", lesson_group.count() , lesson_group, lesson_cabinet)

    class Meta:
        model = Lesson
        fields = ['data', 'subject', 'teacher', 'group', 'time', 'cabinet']

        widgets = {
            "data"  : TextInput(attrs= {
                'type': 'date', 
                'class' :  'form-control'
            }),
            "subject" : Select(attrs={
                'class' :   'form-select',
            }),
            "teacher" : Select(attrs={
                'class' :   'form-select',
            }),
            "group" : Select(attrs={
                'class' :   'form-select',
            }),
            "time" : Select(attrs={
                'class' :   'form-select',
            }),
            "cabinet"  : TextInput(attrs= {
                'class' :  'form-control',
                'placeholder': 'Кабинет'
            }),
        }
