#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from books.models import Book
from books.forms import ContactForm

# Create your views here.
def search_form(request):
    return render_to_response("search_form.html")
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})

def contact(request):
   if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'],cd['message'],cd.get('email','yatcina@mebtorg.ru'),['yatcina@mail.ru'],)
            return HttpResponseRedirect('/contact/thanks/')
   else:
       form = ContactForm(initial={'subject':u'Я люблю этот сайт'})
   return render_to_response('contact_form.html',{'form':form}, RequestContext(request))

def thanks(request):
    c=u"Спасибо, вы успешно вышли из сайта"
    return render_to_response('thanks.html',{'c':c})
def view_books(request):
    books = Book.objects.all()
    return render_to_response('view_books.html',{'books':books})








