# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from ..models import Student

def students_list(request):
    students = Student.objects.all()
    students = students.order_by('last_name', 'ticket', 'last_name', 'id')
    if request.GET.get ('reverse', '') == '1':
	students = students.reverse()
    return render(request, 'students_list.html', {'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
