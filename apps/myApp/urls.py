from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('additem', views.additem),
    path('create', views.create),
    path('add/<int:items_id>', views.add),
    path('item/<int:item_id>', views.displayitem),
    path('delete/<int:item_id>', views.delete),
    path('remove/<int:item_id>', views.remove),
    path('logout', views.logout),
]
