from django.shortcuts import render
from .models import dispmodel
from .forms import appfrom
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

def create_view(request):
    context={}
    form=appfrom(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"create_view.html",context)

def list_view(request):
    context={}
    context["dataset"]=dispmodel.objects.all()
    return render(request,"list_view.html", context)

def detail_view(request,id):
    context={}
    context["data"]=dispmodel.objects.get(id=id)
    return render(request,"detail_view.html",context)


def update_view(request,id):
    context=[]
    obj=get_object_or_404(dispmodel,id=id)
    form=dispmodel(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"]=form
    return render(request,"update_view.html",context)