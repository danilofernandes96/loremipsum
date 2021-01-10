from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.projectList, name='project-list'),
    path('project/<int:id>', views.projectView, name='project-view'),
    path('newproject/', views.newProject, name='new-project'),
    path('edit/<int:id>', views.editProject, name='edit-project'),
    path('delete/<int:id>', views.deleteProject, name='delete-project'),
]