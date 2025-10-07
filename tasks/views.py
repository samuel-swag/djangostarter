from django.shortcuts import render
from .models import Task, Member, Notification


# Create your views here.

def listtasks(request, project):
    tasks = Task.objects.filter(project__name=project)

    return render(request, "tasks/listtasks.html", {
        'project': project,
        'tasks': tasks
    }
    )

def listnotifications(request, username):

    member = Member.objects.filter(username__iexact=username).first()
    notifications = Notification.objects.filter(users__username__iexact=username) if member else []

    return render(request, "tasks/listnotifications.html", {
        'member': username,
        'notifications': notifications,
        'mbr': member
    }
    )

