from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

@login_required
def projectList(request):
    search = request.GET.get('search')
    if search:
        projects = Project.objects.filter(name__icontains=search, user=request.user)
    else:
        projects_list = Project.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(projects_list, 3)
        page = request.GET.get('page')
        projects = paginator.get_page(page)
    return render(request, 'projects/list.html', {'projects': projects})

@login_required
def projectView(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'projects/project.html', {'project': project})

@login_required
def newProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        return render(request, 'projects/addproject.html', {'form': form})

@login_required
def editProject(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=project)

    if(request.method == 'POST'):
        form = ProjectForm(request.POST, instance=project)
        if(form.is_valid()):
            project.save()
            return redirect('/')
        else:
            return render(request, 'projects/editproject.html', {'form': form,  'project': project})
    else:
        return render(request, 'projects/editproject.html', {'form': form,  'project': project})

@login_required
def deleteProject(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    messages.info(request, 'Projeto deletado com sucesso.')

    return redirect('/')

@login_required
def helloworld(request):
    return HttpResponse('Olá mundo')
