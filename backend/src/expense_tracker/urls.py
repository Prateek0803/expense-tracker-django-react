from django.urls import path
from . import views

urlpatterns=[
    path('',views.getView),
    path('add/',views.addExpense)
]