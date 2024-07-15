from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('vacancies/', views.vacancy_list_view, name='vacancy_list'),
    path('vacancies/<int:pk>/', views.vacancy_detail_view, name='vacancy_detail'),
    path('vacancies/create/', views.vacancy_create_view, name='vacancy_create'),
    path('vacancies/<int:pk>/update/', views.vacancy_update_view, name='vacancy_update'),
    path('vacancies/<int:pk>/delete/', views.vacancy_delete_view, name='vacancy_delete'),
    # path('vacancies/search/', views.vacancy_list, name='vacancy_filter'),
    path('resumes/', views.resume_list_view, name='resume_list'),
    path('resumes/<int:pk>/', views.resume_detail_view, name='resume_detail'),
    path('resumes/create/', views.resume_create_view, name='resume_create'),
    path('resumes/<int:pk>/update/', views.resume_update_view, name='resume_update'),
    path('resumes/<int:pk>/delete/', views.resume_delete_view, name='resume_delete'),
]
