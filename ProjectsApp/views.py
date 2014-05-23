from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ProjectsApp.models import Task, Project
import datetime
import os


def all_projects_view(request):
	array_Project = Project.objects.all()
	return render(request, 'projects.html', {'array_Project':array_Project})

def new_project_form(request):
	return render(request,'addProject.html')

def new_project_view(request):
	p = Project(name=request.POST['name'], begin = request.POST['begin'], active=True)
	p.save()
	return HttpResponseRedirect(reverse('ProjectsManagement:new_project_form'))

def all_tasks_view(request):
	array_Project = Project.objects.all()
	array_task = Task.objects.all()
	return render(request, 'tasks.html',{'array_task':array_task})

def new_task_view(request):
	array_Project = Project.objects.all()
	t = Task(name=request.POST['name'],begin = request.POST['begin'] , description= request.POST['description'], project_id = 1, active=True)
	t.save()
	return HttpResponseRedirect(reverse('ProjectsManagement:new_task_form'))

def new_task_form(request):
	return render(request,'newTask.html')

def search_view(request):
	p= Project.objects.all()
	search = Project.objects.filter(name=request.POST['b'])
	return HttpResponseRedirect(reverse('ProjectsManagement:search_form'))

def search_form(request):
	return render(request,'projects.html')

