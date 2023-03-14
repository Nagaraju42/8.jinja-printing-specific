from django.shortcuts import render

# Create your views here.
def Raj(request):
    d={'name':'Thor','age':'25'}
    return render(request,'jinja_print.html',context=d)