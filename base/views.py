from django.shortcuts import render, redirect

from base.forms import ToDoForm
from base.models import ToDo


def create_todo(request):
    if request.method == 'POST':
        post_data = request.Post.copy()

        post_data['is_completed'] = request.Post.get('is_completed') == 'on'

        form = ToDoForm(post_data)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = ToDoForm()
    todos = ToDo.objects.all()
    context = {'form': form, 'todos': todos}
    return render(request, 'base/create.html', context)
