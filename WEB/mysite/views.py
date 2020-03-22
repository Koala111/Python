from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Modi,hello world !You are my family")
    return render(request,'myAPP/index.html')

'''
from .models import Grades
def grades(request):
    #去模型理取数据
    gradesList =Grades.objects.all()
    #将数据传递给模板,模板渲染页面,将渲染好的页面返回给浏览器
    #return render(request,'myApp/index.html',{'grades':gradesList})
    return render(request,'myAPP/index.html')
'''