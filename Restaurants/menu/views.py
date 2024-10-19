from django.shortcuts import render
from menu.models import Menu
# Create your views here.
def func1(request):
    obj=None
    result=Menu.objects.all()
    if request.method=="POST":
        a=request.POST.get('dish_name')
        obj=Menu.objects.filter(dish_name=a)
    return render(request,'index.html',{'res':obj})