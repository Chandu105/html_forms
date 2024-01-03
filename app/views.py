from django.shortcuts import render
from app.models import *
# Create your views here.
def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'create_topic.html')

def webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['n']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'QLWO':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'webpage.html',d)

def AccessRecord(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        name=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']
        WO=Webpage.objects.get(pk=name)
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d1={'QLAO':QLAO}
        return render(request,'display_access.html',d1)
    return render(request,'AccessRecord.html')

def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in tn:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'QLWO':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)

def multiple(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
        name=request.POST.getlist('n')
        QLAO=AccessRecord.objects.none()
        for j in name:
            QLAO=QLAO|AccessRecord.objects.filter(name=j)
        d1={'QLAO':QLAO}
        return render(request,'display_access.html',d1)
    return render(request,'multiple.html',d)


def checkBox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkBox.html',d)