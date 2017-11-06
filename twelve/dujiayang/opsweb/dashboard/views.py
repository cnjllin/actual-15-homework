from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse('<h1>hello django</h1>')
def echart(request):
	name = {'name':'wd'}
	age = {'age':18}
        return render(request,'echart.html',{'name':name,'age' : age})
