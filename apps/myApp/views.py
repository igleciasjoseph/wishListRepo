from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    # User.objects.all().delete()
    return render(request, 'myApp/index.html')


def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            name=request.POST['name'], username=request.POST['username'], datehired = request.POST['datehired'], password=hash)

        request.session['id'] = user.id
        return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(username=request.POST['username'])
        request.session['id'] = user.id
        return redirect('/dashboard')

def dashboard(request):
    if 'id' not in request.session:
        messages.error(request, 'Please log in to enter')
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['id'])
        allitems = List.objects.all()
        myitems = user.lists.all()
        otheritems = allitems.difference(myitems)
        context = {
            'user': user,
            'myitems': myitems,
            'otheritems': otheritems,
        }
        return render(request, 'myApp/dashboard.html', context)
def additem(request):
    return render(request, 'myApp/additem.html')

def create(request):
    user = User.objects.get(id=request.session['id'])
    errors = List.objects.list_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/additem')
    else:
        item = List.objects.create(item=request.POST['item'], creator=user)
        user.lists.add(item)
    return redirect('/dashboard')


def add(request, items_id):
    user = User.objects.get(id=request.session['id'])
    item = List.objects.get(id=items_id)
    user.lists.add(item)
    return redirect('/dashboard')


def displayitem(request, item_id):
    item = List.objects.get(id=item_id)
    user = User.objects.get(id=item.creator.id)
    joiners = item.users.all().exclude(id=user.id)
    context = {
        'item': item,
        'joiners': joiners,
    }
    return render(request, 'myApp/itempage.html', context)


def delete(request, item_id):
    item_to_delete = List.objects.get(id=item_id)
    item_to_delete.delete()
    return redirect('/dashboard')


def remove(request, item_id):
    item = List.objects.get(id=item_id)
    user = User.objects.get(id=request.session['id'])
    user.lists.remove(item)
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')
