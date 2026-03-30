from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from app.models import TaskTable
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# ---------------------- AUTH VIEWS ----------------------

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def register(request):
    user_form = UserCreationForm()
    profile_form = ProfileMF()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileMF(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'registration/register.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')


# ---------------------- TASK CRUD ----------------------

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskMF(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskMF(user=request.user)

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_list(request):
    tasks = TaskTable.objects.filter(
        user=request.user,
        is_deleted=False
    ).order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def update_task(request, pk):
    task = get_object_or_404(
        TaskTable,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        form = TaskMF(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskMF(instance=task, user=request.user)

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(
        TaskTable,
        pk=pk,
        user=request.user
    )

    task.is_deleted = True
    task.save()

    return redirect('task_list')

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryMF(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('create_task')
    else:
        form = CategoryMF()

    return render(request, 'tasks/category_form.html', {'form': form})