from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    Items = Item.objects.order_by("-title")
    Items_by3 = []
    buf = []
    for i in Items:
        buf.append(i)
        if len(buf) == 3:
            Items_by3.append(buf)
            buf = []
    Items_by3.append(buf)
    contex = {
        "Items_by3": Items_by3
    }
    return render(request, "friends/home.html", contex)


def login2(request):
    if not request.user.is_authenticated:

        return render(request, 'friends/form_test.html')
    else:
        logout(request)
        return render(request, "friends/form_test.html")


def submit(request):
    password = request.POST["password"]
    login1 = request.POST["login"]
    if len(password) < 8:
        return redirect(login2)

    user = authenticate(request, username=login1, password=password)

    if user is not None:
        login(request, user)
        return redirect(home)
    else:
        try:
            user = User.objects.create_user(login1, "", password)
            user.save()
            user = authenticate(request, username=login1, password=password)
            request.user = user
            login(request, user)
            return redirect(home)
        except:
            return redirect(login2)


def card(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "friends/detail.html", {"item": item})


def profile(request):
    if not request.user.is_authenticated:
        return redirect(login2)
    else:
        return render(request, "friends/profile.html", {"user": request.user})

def create_item_tool(request):
    a = Item()
    descr = request.POST.get("description", "a")
    image_url = request.POST["image_url"]
    title = request.POST["title"]
    a.description = descr
    a.img_source = image_url
    a.title = title
    a.created_by = request.user.username
    a.save()
    return redirect(home)

def item_creating (request):
    return render(request, "friends/create.html")