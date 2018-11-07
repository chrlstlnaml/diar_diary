from django.shortcuts import render, render_to_response
from .models import Plan, Diary
from .forms import DiaryForm
from django.contrib import auth
from django.utils import timezone

def diary_book(request):

    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
    else:
        form = DiaryForm()

    if request.user.is_authenticated():
        all_diary_lists = Diary.objects.filter(author=request.user).order_by('-date')
        return render(request, 'diary/diary_book.html', {'username': auth.get_user(request).username, 'all_diary_lists': all_diary_lists})
    else:
        return render(request, 'diary/diary_book.html', {'username': auth.get_user(request).username})

def home(request):
    return render(request, 'diary/home.html', {'username': auth.get_user(request).username})

def plan_list(request):
    return render(request, 'diary/plan_list.html', {'username': auth.get_user(request).username})
