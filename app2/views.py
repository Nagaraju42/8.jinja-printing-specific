from django.shortcuts import render

# Create your views here.
def Rani(request):
    d={'name':'Loki','age':24}
    return render(request,'jinja_print.html',context=d)