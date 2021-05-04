from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from scmapp.models import Admin, Event
from datetime import datetime, timedelta, timezone
from django.db.models import Q

# Create your views here.

#User Registration / Login Page
def index(request):
    return render(request,'registration.html')

#Admin Login Page
def admin_login(request):
    return render(request,'admin_login.html')

#Admin Home Page
def admin_home(request):
    if 'aname' in request.session:
        data = {'name':request.session.get('aname')}
        return render(request,'admin_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#To retrieve all events from db 
def admin_event(request):
    if 'aname' in request.session:
        event = Event.objects.all().order_by('-date', '-time')
        data = {'event':event}

        if 'event_status' in request.session:
            data['status'] = request.session.get('event_status')

        return render(request,'admin_event.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin Update Event Page
def update_event(request,id):
    if 'aname' in request.session:
        event = Event.objects.get(eid=id)
        event.date = event.date.strftime('%Y-%m-%d')
        event.time = event.time.strftime('%H:%M:%S')
        data = {'event':event}
        return render(request,'update_event.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin Add Event Page
def add_event(request):
    if 'aname' in request.session:
        return render(request,'add_event.html')
    else:
        return HttpResponse('Something went wrong')

#Admin Logout
def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']

    if 'event_status' in request.session:
        del request.session['event_status']

    return render(request,'admin_login.html')


#For Admin Registration
def atest(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            admin = Admin(name=name,email=email,password=password)
            admin.save()
            # request.session['aname'] = name
            return login_admin(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#For Admin Login
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'admin_login.html',context=data)

        except Exception as e:
            data = {'status':"Invalid Username"}
            return render(request,'admin_login.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")


def db_update_event(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        pname = request.POST.get('pname')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        event = Event.objects.get(eid=id)
        event.name = name
        event.pname = pname
        event.date = date
        event.time = time
        event.duration = duration
        event.save()

        request.session['event_status'] = 'Event updated successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

# For Delete Events
def db_delete_event(request,id):
    if request.method == 'GET':
        event = Event.objects.get(eid=id)
        event.delete()

        request.session['event_status'] = 'Event deleted successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

#To Add Event
def db_add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pname = request.POST.get('pname')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        event = Event(name=name,pname=pname,date=date,time=time,duration=duration)
        event.save()
        request.session['event_status'] = 'Event added successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

# Search Event from db
def admin_search(request):
        data = request.GET['search']
        if data is not None:
            lookups= Q(name__icontains=data) | Q(pname__icontains=data)
        
            event = Event.objects.filter(lookups).order_by('-date', '-time')
            context = {
                'event': event
                    }
            return render(request, 'admin_search.html', context)


#To get the latest events in 7days
def latest(request):
        event = Event.objects.filter(date__gte=datetime.now()-timedelta(days=7)).order_by('date', 'time')
        context = {
            'event': event
        }
        return render(request, 'latest.html', context)

