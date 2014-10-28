# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from ToDoApp.models import ToDo


def todolist(request):
	todolist = ToDo.objects.filter(flag=1)
	finishtodos = ToDo.objects.filter(flag=0)
	return render_to_response('simpleTodo.html',{'todolist':todolist,'finishtodos':finishtodos},context_instance=RequestContext(request))


def todofinish(request,id=''):
	todo = ToDo.objects.get(id=id)
	if todp.flag =='1':
		todo.flag ='0'
		todo.save()
		return HttpResponseRedirect('/simpleTodo/')
	todolist = ToDo.objects.filter(flag=1)
	return render_to_response('simpleTodo.html',{'todplist':todolist},context_instance=RequestContext(request))

def todoback(request,id=''):
	todo = ToDo.objects.get(id=id)
	if todo.flag =='0':
		todo.flag ='1'
		todo.save()
		return HttpResponseRedirect('/simpleTodo/')
	todolist = ToDo.objects.filter(flag=1)
	return render_to_response('simpleTodo.html',{'todplist':todolist},context_instance=RequestContext(request))

def tododelete(request,id=''):
	try:
		todo = ToDo.objects.get(id=id)
	except Exception:
		Http404
	if todo:
		todo.delete()
		return HttpResponseRedirect('/simpleTodo/')
	todolist = ToDo.objects.filter(flag=1)
	return render_to_response('simpleTodo.html',{'todplist':todolist},context_instance=RequestContext(request))

def addTodo(request):
	if request.method =='POST':
		atodo = request.POST['todo']
		priority = request.POST['priority']
		user =User.objects.get(id='1')
		todo = ToDo(user=user, todo = atodo, priority=priority, flag=1)
		todo.save()
		todolist = ToDo.objects.filter(flag=1)
		finishtodos = todolist = ToDo.objects.filter(flag=0)
		return render_to_response('showtodo.html',{'todolist':todolist, 'finishtodos':finishtodos},context_instance=RequestContext(request))
	else:
		todolist = ToDo.objects.filter(flag=1)
		finishtodos = ToDo.objects.filter(flag=0)
		return render_to_response('simpleTodo.html',{'todolist':todolist, 'finishtodos':finishtodos})


def updatetodo(request,id=''):
	if request.method == 'POST':
		atodo = request.POST['todo']
		priority = request.POST['priority']
		user = User.objects.get(id='1')
		todo = ToDo(user=user, todo=atodo, priority=priority, flag=1)
		todo.save()
		todolist = ToDo.objects.filter(flag=1)
		finishtodos = ToDo.objects.filter(flag=0)
		return render_to_response('simpleTodo.html',{'todolist':todolist, 'finishtodos':finishtodos})
	else:
		try:
			todo = ToDo.objects.get(id=id)
		except Exception:
			raise Http404
		return render_to_response('updatetodo.html', {'todo':todo}, context_instance=RequestContext(request))
