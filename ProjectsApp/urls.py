from django.conf.urls import patterns, include, url
from ProjectsApp import views


urlpatterns = patterns('',
    url(r'^allprojects$', views.all_projects_view, name='allprojects'),
    url(r'^alltask$', views.all_tasks_view, name='alltask'),
    url(r'^addproject$', views.new_project_view, name='new_project_view'),
    url(r'^created$',views.new_project_form, name='new_project_form'),
    url(r'^addtask$', views.new_task_view, name='new_task_view'),
    url(r'^createdt$',views.new_task_form, name='new_task_form'),
 )