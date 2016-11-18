from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Controller
from .models import Question,Choice

def welcome(request):
    question_list=Question.objects.all()
    print(question_list)
    return render(request,'pollsapp/index.html',{'question_list':question_list})
    #return HttpResponse('this is home page testing this')

def detail(request,questionid):
    question=Question.objects.get(pk=questionid)
    return render(request,'pollsapp/detail.html',{'question':question})

def vote(request,questionid):
    selectedchoice=request.POST['choice']
    choice=Choice.objects.get(pk=selectedchoice)
    choice.votes+=1
    choice.save()
    question=Question.objects.get(pk=questionid)
    return render(request,'pollsapp/results.html',{'question':question})