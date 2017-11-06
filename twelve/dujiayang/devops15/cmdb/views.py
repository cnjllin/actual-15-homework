from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	#return HttpResponse('<h1>hello django</h1>')
	name = {'name':'wd'}
	return render(request,'cmdb/index.html',{'name':name})

def idc(request):
	#return HttpResponse('<h1>hello idc</h1>')
	return render(request,'cmdb/idc_list.html',{'result':result})

def server(request):
	return HttpResponse('<h1>hello server</h1>')
