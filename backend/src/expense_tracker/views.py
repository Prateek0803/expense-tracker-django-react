from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Expenses
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def getView(request):
    data = Expenses.objects.all()
    return JsonResponse(data,safe=False)

@csrf_exempt
def addExpense(request):
    data = json.loads(request.body)
    title = data.get('title')
    amount = data.get('amount')
    category = data.get('category')
    sub_category = data.get('sub_category')
    payment = data.get('payment')

    expense = Expenses(title = title, amount = amount, category = category, sub_category = sub_category,payment = payment)
    expense.save()
    return JsonResponse({'status code': 200 , 'message' : 'saved successfully'})

