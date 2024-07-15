from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from main_APP.forms import VacancyUpdateForm, VacancyCreateForm, ResumeUpdateForm, ResumeCreateForm, VacancyFilterForm
from main_APP.models import Vacancy, Resume


# Create your views here.

def start_page(request):
    return render(request, 'main_APP/start_page.html',context={'user': request.user})

@login_required(login_url='login_page')
def vacancy_list_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'main_APP/vacancy_list.html', {'vacancies': vacancies})


@login_required(login_url='login_page')
def vacancy_detail_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'main_APP/vacancy_detail.html', {'vacancy': vacancy})


@login_required(login_url='login_page')
def resume_list_view(request):
    resumes = Resume.objects.all()
    return render(request, 'main_APP/resume_list.html', {'resumes': resumes})


@login_required(login_url='login_page')
def resume_detail_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'main_APP/resume_detail.html', {'resume': resume})


@login_required(login_url='login_page')
def resume_create_view(request):
    if request.method == 'POST':
        form = ResumeCreateForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list')
    else:
        form = ResumeCreateForm()
    return render(request, 'main_APP/resume_create.html', {'form': form})


@login_required(login_url='login_page')
def resume_update_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        form = ResumeUpdateForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeUpdateForm(instance=resume)
    return render(request, 'main_APP/resume_update.html', {'form': form})


@login_required(login_url='login_page')
def resume_delete_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.delete()
    return redirect('resume_list')


@login_required(login_url='login_page')
@staff_member_required(login_url='')
def vacancy_create_view(request):
    if request.method == 'POST':
        form = VacancyCreateForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.user = request.user
            vacancy.save()
            return redirect('vacancy_list')
    else:
        form = VacancyCreateForm()
    return render(request, 'main_APP/vacancy_create.html', {'form': form})


@login_required(login_url='login_page')
@staff_member_required
def vacancy_update_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        form = VacancyUpdateForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyUpdateForm(instance=vacancy)
    return render(request, 'main_APP/vacancy_update.html', {'form': form})


@login_required(login_url='login_page')
@staff_member_required
def vacancy_delete_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.delete()
    return redirect('vacancy_list')


# @login_required(login_url='login_page')
# @staff_member_required
# def vacancy_list(request,pk):
#     form = VacancyFilterForm(request.GET)
#     vacancies = Vacancy.objects.all()
#
#     if form.is_valid():
#         employer = form.cleaned_data.get('employer')
#         if employer:
#             vacancies = vacancies.filter(employer=employer)
#
#     context = {
#         'form': form,
#         'vacancies': vacancies
#     }
#     return render(request, 'main_APP/vacansy_list_staff.html', context)