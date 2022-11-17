from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="india"
    return render(request,"input.html",{'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,"result.html",{"result1":add,"result2":sub,"result3":mul,"result4":div})

