from base.forms import ToDoForm, MyUserCreationForm
from base.models import ToDo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('create')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, message='User does not exit')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('create')
        else:
            messages.error(request, message="Username or Password doesn't exit")

    context = {'page': page}
    return render(request, template_name='login_register.html', context=context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # save the data in database
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('create')
        else:
            messages.error(request, message='An error occurred during registration')

    return render(request, template_name='login_register.html', context={'form': form})


def create_todo(request):
    if request.method == 'POST':
        post_data = request.POST.copy()

        post_data['is_completed'] = request.POST.get('is_completed') == 'on'

        form = ToDoForm(post_data)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = ToDoForm()
    todos = ToDo.objects.all()
    context = {'form': form, 'todos': todos}
    return render(request, 'create.html', context)


# get compare the value in single row

