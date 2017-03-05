from django.shortcuts import redirect, render

import forum.models

import math

_MESSAGES_PER_PAGE = 20


def index(request):
    categories = forum.models.Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def category(request, category_id):
    category = forum.models.Category.objects.get(id=category_id)
    return render(request, 'category.html', {'category': category})


def thread(request, thread_id, page_num):
    thread = forum.models.Thread.objects.get(id=thread_id)
    total_page_count = math.ceil(float(len(thread.message_set.all())) / _MESSAGES_PER_PAGE)
    min_message_id = int(page_num) * _MESSAGES_PER_PAGE
    max_message_id = min_message_id + _MESSAGES_PER_PAGE + 1
    messages = thread.message_set.filter(id__gt=min_message_id).filter(id__lt=max_message_id)
    #messages = forum.models.Message.objects().filter(thread=thread.id).filter(id__gt=min_message_id).filter(id__lt=max_message_id)
    return render(request, 'thread.html', {'thread': thread, 'messages': messages, 'total_page_count': total_page_count})


def profile(request, profile_id):
    return render(request, 'profile.html')
