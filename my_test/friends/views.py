from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Item, Comments
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import sqlite3

from .file_handler import handle_uploaded_file


def home(request):
    name = request.POST.get("request")
    tag = request.POST.get("tag")

    if name is not None:
        Items_original = Item.objects.order_by("-title")
        Items = []
        if tag != "Выберите вид рецепта":
            for i in Items_original:
                if name.lower() in i.title.lower() and i.tag == tag:
                    Items.append(i)
        else:
            for i in Items_original:
                if name.lower() in i.title.lower():
                    Items.append(i)
        Items_by3 = []
        buf = []
        for i in Items:
            buf.append(i)
            if len(buf) == 3:
                Items_by3.append(buf)
                buf = []
        Items_by3.append(buf)
        contex = {
            "user": request.user,
            "Items_by3": Items_by3
        }

        return render(request, "friends/home.html", contex)
    else:
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
    delete = request.POST.get("delete")
    comment_text = request.POST.get("comment")
    if delete is not None:
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return redirect(home)
    else:
        if comment_text is not None:
            com = Comments()
            com.created_by = request.user.username
            com.comment_text = comment_text
            com.related_to = get_object_or_404(Item, pk=item_id)
            com.save()
            return redirect(home)
        item = get_object_or_404(Item, pk=item_id)
        comments = Comments.objects.filter(related_to=item)



        buf = []
        for i in item.ingredients.split("$"):
            buf.append(i.split("|"))

        return render(request, "friends/detail.html", {"item": item, "user": request.user, "Pairs": buf[:len(buf)-1], "Comments":comments})


def profile(request):
    if not request.user.is_authenticated:
        return redirect(login2)
    else:
        return render(request, "friends/profile.html", {"user": request.user})


# def create_item_tool(request):
#     a = Item()
#     while True:
#         i = 0
#         if request.POST.get("ingr_name" + str(i)) is not None:
#             a.buf = request.POST.get("ingr_name" + str(i)) + "|" + request.POST.get("ingr_value" + str(i))
#             a.ingr.append(a.buf)
#         else:
#             break
#         i += 1
#     descr = request.POST.get("description", "a")
#     image_url = request.POST["image_url"]
#     title = request.POST["title"]
#     tag = request.POST["tag"]
#     image = request.POST["image"]
#
#     a.description = descr
#     a.img_source = image_url
#     a.title = title
#     a.tag = tag
#     a.image = image
#     a.created_by = request.user.username
#     a.save()
#     return redirect(home)
#
#
# def creat_validation(request):
#     return render(request, "friends/create_valid.html")
#
#
# def item_creating(request):
#     amount = request.POST["amount"]
#     contex = {
#         "Range": range(int(amount))}
#
#     return render(request, "friends/create.html", contex)


def create(request):

    amount = request.POST.get("amount")

    if request.POST.get("amount") is None and request.POST.get("title") is None:
        return render(request, "friends/create_rework1page.html")
    elif request.POST.get("amount") is not None and request.POST.get("title") is None:
        contex = {"amount": range(1, int(amount)+1)}
        return render(request, "friends/create_rework2page.html", context=contex)
    else:
        a = Item()
        a.title = request.POST.get("title")
        a.tag = request.POST.get("tag")
        a.description = request.POST.get("description")
        a.created_by = request.user.username
        a.img_source = request.POST.get("image_url")
        buf1=""
        buf2=""
        i=1
        while request.POST.get("ingr-name"+str(i)) is not None:
            buf1 += request.POST.get("ingr-name"+str(i))
            buf1 += "|"
            buf1 += request.POST.get("ingr-value"+str(i))
            buf2 += buf1 + "$"
            buf1=""
            i+=1
        a.ingredients = buf2
        a.save()
        return redirect(home)



def testing_expample(request):
    return render(request, "friends/testing.html")


def info(request):
    return render(request, "friends/info.html")


def searching(request):
    req = request.POST["request"]
    return HttpResponse(req)
