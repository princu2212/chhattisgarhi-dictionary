from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import dictionary
from app1.models import Contact, AddWord
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    
def search(request):
    query = request.GET.get('search')
    word = AddWord.objects.filter(hindi__contains = query)
    return render(request, 'index.html', {'word': word})


def services(request):
    if request.method == 'POST':
        fm = dictionary(request.POST)
        if fm.is_valid():
            hi = fm.cleaned_data['hindi']
            en = fm.cleaned_data['english']
            cg = fm.cleaned_data['chhattisgarhi']
            reg = AddWord(hindi=hi, english=en, chhattisgarhi=cg)
            reg.save()
            fm = dictionary()
            messages.success(request, 'Successfully Added.')
    else:
        fm = dictionary()
    add = AddWord.objects.all()
    return render(request, 'services.html', {'form': fm, 'dict': add})

def about(request):
    return render(request, 'about.html')
        
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        contact = Contact(name = name, email = email, query = query)
        contact.save()
        messages.success(request, 'your message has been sent.')
    return render(request, 'contact.html')

 




