from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse  
# Intro example
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

# View example 1
import datetime  
# Create your views here.  
# from django.http import HttpResponse  
# def index(request):  
#     now = datetime.datetime.now()  
#     html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
#     return HttpResponse(html)    # rendering the template in HttpResponse 

# # View example 2
# from django.http import HttpResponse, HttpResponseNotFound  
# def index(request):  
#     a = 1  
#     if a:  
#         return HttpResponseNotFound('<h1>Page not found</h1>')  
#     else:  
#         return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse 
    
    
# View Example 3--decorators
# from django.shortcuts import render  
# Create your views here.  
# from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  



# Templates

# from django.shortcuts import render  
# #importing loading from django template  
# from django.template import loader  
# # Create your views here.  
# from django.http import HttpResponse  
# def index(request):  
#    template = loader.get_template('index.html') # getting our template  
#    name = {  
#         'student':'Rahul'  
#     }
#    return HttpResponse(template.render(name))       # rendering the template in HttpResponse

# # Image Loading Example
# def index(request):  
#     return render(request,'index1.html')


# JavaScript Loading Example
def index(request):  
    return render(request,'index_script.html')


# CSS Loading Example
def index(request):  
    return render(request,'index_css.html')
