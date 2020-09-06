from django.http import HttpResponseRedirect
from django.shortcuts import render
import guestbook.models as guestbookmodels
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hello World</h1>', content_type='text/html')
    results = guestbookmodels.fetchlist()
    data = {'guestbooklist': results }
    return render(request, 'guestbook/index.html', data)

def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    guestbookmodels.insert(name, password, message)

    return HttpResponseRedirect('/guestbook')




def deleteform(request):
    return render(request,'guestbook/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    guestbookmodels.delete(no, password)

    return HttpResponseRedirect('/guestbook')