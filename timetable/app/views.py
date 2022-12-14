from calendar import month
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Lesson, Group, Subject, Teacher, Speciality, Time
from datetime import date, timedelta, datetime
from .forms import CalendarFilterForm, SubjectForm, TeacherForm, SpecialityForm, GroupForm, TimeForm, LessonForm
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")

class CalendarDay:
    data = None
    lessons = []
    name = None

    def __init__(self, data, name, group, teacher):
        self.name = name
        self.data = data
        self.lessons = Lesson.objects.filter(
            data__year= data.year,
            data__month= data.month,
            data__day = data.day,
        )
        if (teacher):
            self.lessons = self.lessons.filter(
                teacher_id = teacher
        )

        if (group):
            self.lessons = self.lessons.filter(
                group__id = group
        )
        self.lessons.order_by('time')

def getWeekParams (monday, group, teacher):
    params = [f'week={monday}']

    if (group):
        params.append(f'group={group}')

    if (teacher):
        params.append(f'teacher={teacher}')

    return '&'.join(params)
    

def index(request):
    week = request.GET.get("week")
    group_id = request.GET.get("group")
    teacher_id = request.GET.get("teacher")
    isEmpty = not (group_id or teacher_id)
    today = date.today()
    
    if (week) : 
        monday = datetime.strptime(week, '%d.%m.%Y')

    else : 
        monday = today - timedelta(days=today.weekday())

    if (request.POST):
        group_id = request.POST.get("group", "0")
        teacher_id = request.POST.get("teacher", "0")
        
        return redirect(f'/?{getWeekParams(monday.strftime("%d.%m.%Y"), group_id, teacher_id)}')

    form = CalendarFilterForm({'teacher':teacher_id, 'group':group_id})

    groups = Group.objects.all()
    teachers = Teacher.objects.all()

    calendar = (
        CalendarDay(monday, "Понедельник", group_id , teacher_id),
        CalendarDay(monday + timedelta(days=1), "Вторник", group_id, teacher_id),
        CalendarDay(monday + timedelta(days=2), "Среда", group_id, teacher_id),
        CalendarDay(monday + timedelta(days=3), "Четверг", group_id, teacher_id),
        CalendarDay(monday + timedelta(days=4), "Пятница", group_id, teacher_id),
        CalendarDay(monday + timedelta(days=5), "Суббота", group_id, teacher_id),
        CalendarDay(monday + timedelta(days=6), "Воскресенье", group_id, teacher_id),
    )

    data = {
        'month': (monday + timedelta(days=3)).strftime("%B %Y"),
        'monday' : monday,
        'thisweek' : getWeekParams((today - timedelta(days=today.weekday())).strftime("%d.%m.%Y"), group_id, teacher_id),
        'pastweek': getWeekParams((monday - timedelta(days=7)).strftime("%d.%m.%Y"), group_id, teacher_id),
        'nextweek' : getWeekParams((monday + timedelta(days=7)).strftime("%d.%m.%Y"), group_id, teacher_id),
        'groups': groups,
        'teachers': teachers,
        'calendar': calendar,
        'form' : form,
        'isEmpty' : isEmpty
    }

    return render(request, 'home.html', data)


# Предмет

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subject-new.html'
    form_class = SubjectForm

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subject-new.html'
    form_class = SubjectForm

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url= '/options/subject'
    template_name = 'subject-delete.html'

# Преподаватель

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher-new.html'
    form_class = TeacherForm

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher-new.html'
    form_class = TeacherForm

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url= '/options/teacher'
    template_name = 'teacher-delete.html'

# Специальность

class SpecialityCreateView(CreateView):
    model = Speciality
    template_name = 'speciality-new.html'
    form_class = SpecialityForm

class SpecialityUpdateView(UpdateView):
    model = Speciality
    template_name = 'speciality-new.html'
    form_class = SpecialityForm

class SpecialityDeleteView(DeleteView):
    model = Speciality
    success_url= '/options/speciality'
    template_name = 'speciality-delete.html'

# Группа

class GroupCreateView(CreateView):
    model = Group
    template_name = 'group-new.html'
    form_class = GroupForm

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group-new.html'
    form_class = GroupForm

class GroupDeleteView(DeleteView):
    model = Group
    success_url= '/options/group'
    template_name = 'group-delete.html'

# Время

class TimeCreateView(CreateView):
    model = Time
    template_name = 'time-new.html'
    form_class = TimeForm

class TimeUpdateView(UpdateView):
    model = Time
    template_name = 'time-new.html'
    form_class = TimeForm

class TimeDeleteView(DeleteView):
    model = Time
    success_url= '/options/time'
    template_name = 'time-delete.html'

# Занятие

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'lesson-new.html'
    form_class = LessonForm

class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'lesson-new.html'
    form_class = LessonForm

class LessonDeleteView(DeleteView):
    model = Lesson
    success_url= '/options/lesson'
    template_name = 'lesson-delete.html'

def multipleDeletion(request, model):
    if request.method == 'POST':
        deleting_id = []
        for key in request.POST.keys():
            if key != "csrfmiddlewaretoken":
                deleting_id.append(int(key))
        model.objects.filter(id__in = deleting_id).delete()

def options (request):
    return render(request, 'options.html')

def subjects(request):
    subjects = Subject.objects.order_by('name')
    multipleDeletion(request, Subject)

    data = {
        'subjects' : subjects
    }
    return render(request, 'subject.html', data)

def teachers(request):
    teachers = Teacher.objects.order_by('surname')
    multipleDeletion(request, Teacher)
    data = {
        'teachers' : teachers
    }
    return render(request, 'teacher.html', data)

def specialityes(request):
    specialityes = Speciality.objects.order_by('title')
    multipleDeletion(request, Speciality)
    data = {
        'specialityes' :  specialityes
    }
    return render(request, 'speciality.html', data)

def groups(request):
    groups = Group.objects.order_by('course')
    multipleDeletion(request, Group)
    data = {
        'groups' : groups
    }
    return render(request, 'group.html', data)

def times(request):
    times = Time.objects.order_by('name')
    multipleDeletion(request, Time)
    data = {
        'times' : times
    }
    return render(request, 'time.html', data)



def lessons(request):
    lessons = Lesson.objects.order_by('data')
    multipleDeletion(request, Lesson)
    data = {
        'lessons' : lessons
    }
    return render(request, 'lesson.html', data)
