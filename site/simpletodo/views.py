#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

def index(request):
    ctx = {}
    ctx['todos'] = Todo.objects.all().order_by('finished', '-id')
    ctx['form'] = TodoForm()
    return render(request, 'index.html', ctx)

def new(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, u'创建成功')
            return HttpResponseRedirect(reverse("todo_idx"))
    return render(request, 'todo/form.html', {'form': form})


def edit(request, id):
    edit_todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=edit_todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=edit_todo)
        if form.is_valid():
            form.save()
            messages.info(request, u'编辑成功')
            return HttpResponseRedirect(reverse("todo_idx"))
    return render(request, 'todo/form.html', {'form': form})

def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    messages.info(request, u'成功删除')
    return HttpResponseRedirect(reverse("todo_idx"))

def finish(request, id):
    todo = get_object_or_404(Todo, id=id)
    status = request.GET.get('status', '')
    if status == 'yes':
        finished = 1
        todo.finished = finished
    elif status == 'no':
        finished = 0
    else:
        messages.info(request, u'非法请求')
        return HttpResponseRedirect(reverse("todo_idx"))
    todo.finished = finished
    todo.save()
    messages.info(request, u'修改成功')
    return HttpResponseRedirect(reverse("todo_idx"))
