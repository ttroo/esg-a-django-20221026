from django.shortcuts import render, redirect

from diary.models import Diary
from diary.forms import DiaryForm


def memory_list(request):
    everything = Diary.objects.all().order_by("-id")
    return render(request, "diary/memory_list.html", {"all_about" : everything,})

def memory_detail(request, pk):
    only_one = Diary.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {"only_one" : only_one,})

def memory_new(request):
    if request.method == "GET":
        form_type = DiaryForm()
    else:
        form_type = DiaryForm(request.POST)
        if form_type.is_valid():
            diary = form_type.save()
            return redirect(diary)

    return render(request, "diary/memory_new.html", {"form_type" : form_type,})

##############################

def memory_edit(request, pk):
    memory = Diary.objects.get(pk=pk)
    if request.method == "GET":
        form_type = DiaryForm(instance=memory)
    else:
        form_type = DiaryForm(request.POST, instance=memory)
        if form_type.is_valid():
            diary = form_type.save()
            return redirect(diary)

    return render(request, "diary/memory_new.html", {"form_type" : form_type,})