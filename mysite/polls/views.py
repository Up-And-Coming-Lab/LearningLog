from django.shortcuts import render,get_object_or_404
from django.http import Http404
#from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    #try:
    #   question = Question.objects.get(pk=question_id)
    #except Question.DoseNotExist: #ObjectDoesNotExist
    #   raise Http404("问题不存在")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "你所查看该问题的结果 %s."
    return HttpResponse(response % question_id)
	
def vote(request,question_id):
    return HttpResponse("你所投票的问题为 %s." % question_id)