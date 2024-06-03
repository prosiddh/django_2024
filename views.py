from django.shortcuts import render
from django.http import HttpResponse

def HomeAppDef(request):
    peoples=[
        {'name':'Prasiddh', 'age':25},
        {'name':'Jay', 'age':21},
        {'name':'VK', 'age':22}
    ]
    vegetables=['Mango','Banana']
    context={'peoples':peoples,'vegetables':vegetables,'page':'Home of Django'}
    return render (request,"home/index.html",context)

def success_page(request):
    return HttpResponse("This is success page")

def contact_page(request):
    context={'page':'Contact'}
    return render(request,"home/contact.html",context)

def about_page(request):
    context={'page':'About'}
    return render(request,"home/about.html",context)