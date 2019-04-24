from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .form import StudentForm
# Create your views here.
from student.models import Student
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        words = 'world!'
        context = {'words': words, 'students': students}
        return context

    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form':form})
        return render(request,self.template_name,context=context)

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form':form})
        return render(request, self.template_name, context=context)