from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

import forum.models

import math
import json

_MESSAGES_PER_PAGE = 20


def index(request):
    categories = forum.models.Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def category(request, category_id):
    category = forum.models.Category.objects.get(id=category_id)
    return render(request, 'category.html', {'category': category})


def thread(request, thread_id, page_num):
    thread = forum.models.Thread.objects.get(id=thread_id)
    total_page_count = int(math.ceil(float(len(thread.message_set.all())) / _MESSAGES_PER_PAGE))
    min_message_id = int(page_num) * _MESSAGES_PER_PAGE
    max_message_id = min_message_id + _MESSAGES_PER_PAGE + 1
    messages = thread.message_set.filter(id__gt=min_message_id).filter(id__lt=max_message_id)
    return render(request, 'thread.html', {'thread': thread, 'page_num': page_num,
                                           'total_page_count': total_page_count})


def profile(request, profile_id):
    return render(request, 'profile.html')


@login_required
def send_message(request, thread_id):
    thread = forum.models.Thread.objects.get(id=thread_id)
    message = request.POST['message']
    forum.models.Message(thread=thread, text=message, author=request.user).save()
    last_page_num = int(math.ceil(float(len(thread.message_set.all())) / _MESSAGES_PER_PAGE)) - 1
    return redirect('thread', thread.id, last_page_num)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })


def load_messages(request):
    '''
    Ajax request.
    Params:
        thread_id, page_num
    Return: {
        'messages': ...
    }
    '''

    thread = forum.models.Thread.objects.get(id=int(request.GET['thread_id']))
    total_page_count = math.ceil(float(len(thread.message_set.all())) / _MESSAGES_PER_PAGE)
    min_message_id = int(request.GET['page_num']) * _MESSAGES_PER_PAGE
    max_message_id = min_message_id + _MESSAGES_PER_PAGE + 1
    messages = thread.message_set.filter(id__gt=min_message_id).filter(id__lt=max_message_id)

    messages_json = [message.as_dict() for message in messages]

    response_data = {
        'messages': messages_json
    }

    return HttpResponse(json.dumps(response_data), content_type='application/json')
