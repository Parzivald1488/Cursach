from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('options/', views.options , name='options'),

    path('options/subject', views.subjects , name='subject'),
    path('options/subject/', views.SubjectCreateView.as_view(), name='subject-new'),
    path('options/subject/<int:pk>/update', views.SubjectUpdateView.as_view(), name='subject-update'),
    path('options/subject/<int:pk>/delete', views.SubjectDeleteView.as_view(), name='subject-delete'),

    path('options/teacher', views.teachers , name='teacher'),
    path('options/teacher/', views.TeacherCreateView.as_view(), name='teacher-new'),
    path('options/teacher/<int:pk>/update', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('options/teacher/<int:pk>/delete', views.TeacherDeleteView.as_view(), name='teacher-delete'),

    path('options/speciality', views.specialityes , name='speciality'),
    path('options/speciality/', views.SpecialityCreateView.as_view(), name='speciality-new'),
    path('options/speciality/<int:pk>/update', views.SpecialityUpdateView.as_view(), name='speciality-update'),
    path('options/speciality/<int:pk>/delete', views.SpecialityDeleteView.as_view(), name='speciality-delete'),

    path('options/group', views.groups , name='group'),
    path('options/group/', views.GroupCreateView.as_view(), name='group-new'),
    path('options/group/<int:pk>/update', views.GroupUpdateView.as_view(), name='group-update'),
    path('options/group/<int:pk>/delete', views.GroupDeleteView.as_view(), name='group-delete'),

    path('options/time', views.times , name='time'),
    path('options/time/', views.TimeCreateView.as_view(), name='time-new'),
    path('options/time/<int:pk>/update', views.TimeUpdateView.as_view(), name='time-update'),
    path('options/time/<int:pk>/delete', views.TimeDeleteView.as_view(), name='time-delete'),

    path('options/lesson', views.lessons , name='lesson'),
    path('options/lesson/', views.LessonCreateView.as_view(), name='lesson-new'),
    path('options/lesson/<int:pk>/update', views.LessonUpdateView.as_view(), name='lesson-update'),
    path('options/lesson/<int:pk>/delete', views.LessonDeleteView.as_view(), name='lesson-delete'),
]