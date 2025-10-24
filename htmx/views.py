from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
import random
from tasks.models import Notification, Project, Task, Member
from htmx.models import Response

# Read the URLs for NASA images
imageurls = open("static/nasa_imageurls").readlines()

def randomimg():
    return { 
            'image': random.choice(imageurls).strip()
    }


def assignment(request):
    if request.method == 'GET':
        return render(request, "htmx/assignment.html", {})
    else:
        memberID = request.POST['memberID']
        search_type = request.POST['dropdown']

        if search_type == 'tasks':
            valid = False
            has_tasks = False
            member = Member.objects.filter(username__iexact=memberID).first()
            tasks = Task.objects.filter(assignee__username__iexact=memberID) if member else []
            if member:
                valid = True
            if tasks != []:
                has_tasks = True
            return render(request, "htmx/partials/assignment_tasks.html", {
                'valid': valid,
                'has_tasks': has_tasks,
                'tasks': tasks,
                'member': memberID
            })
        else:
            valid = False
            has_notifs = False
            member = Member.objects.filter(username__iexact=memberID).first()
            if member:
                valid = True
            notifications = Notification.objects.filter(users__username__iexact=memberID) if member else []
            if notifications != []:
                has_notifs = True
            return render(request, "htmx/partials/assignment_notifications.html", {
                'valid': valid,
                'has_notifs': has_notifs,
                'notifications': notifications,
                'member': memberID
            })
        #return HttpResponse(f"The number is {'even' if memberID % 2 == 0 else 'odd'}")

@require_GET
def demo(request):
    return render(request,'htmx/demo.html', randomimg())

@require_GET
def demo_bootstrap(request):
    return render(request,'htmx/demo_bootstrap.html', {})


# POST request example
@require_POST
def answer(request):
    try:
        value = int(request.POST['value'])
        func = request.POST['function']
        if func == "square":
            return render(request, "htmx/partials/answer.html", {'answer': value*value })
        else:
            return render(request, "htmx/partials/answer.html", {'answer': value*value*value })
    except:
        return render(request, "htmx/partials/answer.html",{'answer': "Invalid"})
    

@require_POST
def answer1(request):
    try:
        value = int(request.POST['value1'])
        func = request.POST['function1']
        if func == "square":
            return render(request, "htmx/partials/answer.html", {'answer': value*value })
        else:
            return render(request, "htmx/partials/answer.html", {'answer': value*value*value })
    except:
        return render(request, "htmx/partials/answer.html",{'answer': "Invalid"})

@require_GET
def oneimage(request):
    return render(request, 'htmx/partials/image.html', randomimg())

@require_GET
def example1(request):
    return render(request, 'htmx/example1.html', {})

@require_GET
def example2(request):
    return render(request, 'htmx/example2.html', {})

@require_GET
def example3(request):
    return render(request, 'htmx/example3.html', randomimg())

@require_GET
def example4(request):
    return render(request, 'htmx/example4.html', {
        'projects': Project.objects.all()
    })

@require_POST
def tasks4project(request):
    try:
        id = int(request.POST['id'])
        tasks = Task.objects.filter(project__id=id)
        return render(request, "htmx/partials/tasks.html", {
            'tasks': tasks            
        })
    except:
        return render(request, "htmx/partials/tasks.html", {
            'tasks': []             
        })
    
@require_GET
def member4task(request, id):
    try:
        # name = int(request.POST['name'])
        task = Task.objects.get(id=id)
        return render(request, "htmx/partials/member.html", {
            'member': task.assignee          
        })
    except:
        return render(request, "htmx/partials/member.html", {
            'member': []             
        })


@require_GET
def jsdemo(request):
    return render(request, "htmx/jsdemo.html", {})


@require_POST
def jsresponse(request):
    times = request.POST['times']
    responses = times.split(" ")
    previous = int(responses[0])
    responses.pop(0)
    answer = "Server received: "
    buttons = []
    latencies = []
    prev = previous

    for response in responses:
        values = response.split(':')
        button = values[0]
        timestamp = int(values[1])
        latency = (timestamp - prev)/1000

        buttons.append(button)
        latencies.append(latency)
        prev = timestamp
        if len(buttons) == 1:
            answer = f"{answer} Button {button} after a latency of {latency} seconds. "
        else:
            answer = f"{answer} Button {button} after an additional {latency} seconds. "

    Response.objects.create(
        # Record button responses
        button1=buttons[0] if len(buttons) > 0 else '',
        button2=buttons[1] if len(buttons) > 1 else '',
        button3=buttons[2] if len(buttons) > 2 else '',
        # Record latencies
        latency1=latencies[0] if len(latencies) > 0 else '',
        latency2=latencies[1] if len(latencies) > 1 else '',
        latency3=latencies[2] if len(latencies) > 2 else '',

    )

    all_responses = Response.objects.all().order_by('-timestamp')[:10]
    return render(request, "htmx/partials/times.html",{
        'answer': answer,
        'all_responses': all_responses
    }) 
