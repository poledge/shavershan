from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shavershan.models import feed, order
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
import json


def add_order(request):
    if request.user.is_authenticated:

        customer = User.objects.filter(username = request.user)[0]

        check_order = None

        try:
            check_order = order.objects.filter(customer = customer).filter(feed = request.POST["id"])[0]
        except:
            pass

        if check_order:
            count = check_order.count + 1
            check_order.count = count
            check_order.save()
        else:       
            order.objects.create(customer = customer, feed = feed.objects.filter(id = request.POST["id"])[0], count = 1)

        orders_count = str(len(order.objects.filter(customer = request.user)))

        error = 'Товар добавлен в корзину'
    else:
        error = 'Вы не зарегистрированы'

        orders_count = ''

    responseData = {
        'error': error,
        'orders_count': orders_count
    }

    return JsonResponse(responseData)

def get_orders_count(request):
    if request.user.is_authenticated:
        
        orders_count = str(len(order.objects.filter(customer = request.user)))

        error = 'Количество заказов'
    else:
        error = 'Вы не зарегистрированы'

        orders_count = ''

    responseData = {
        'error': error,
        'orders_count': orders_count
    }

    return JsonResponse(responseData)

def del_order(request):
    if request.user.is_authenticated:

        order.objects.filter(id = request.POST["id"]).delete()

        error = 'Все норм'
    else:
        error = 'Вы не зарегистрированы'

    responseData = {
        'error': error
    }

    return JsonResponse(responseData)

def update_order(request):
    if request.user.is_authenticated:

        customer = User.objects.filter(username = request.user)[0]

        check_order = None

        try:
            check_order = order.objects.filter(customer = customer).filter(id = request.POST["id"])[0]
        except:
            pass

        if check_order:
            check_order.count = request.POST["count"]
            check_order.save()

            error = 'Все норм'
        else:
            error = 'Заказ не найден'

    else:
        error = 'Вы не зарегистрированы'

    responseData = {
        'error': error
    }

    return JsonResponse(responseData)

def confirm_all(request):
    if request.user.is_authenticated:
        customer = User.objects.filter(username = request.user)[0]

        check_order = None

        try:
            check_order = order.objects.filter(customer = customer)
            print(check_order)
        except:
            pass

        if check_order:
            for i in check_order:
                i.confirmed = True
                i.save()

        error = 'Все норм'
    else:
        error = 'Вы не зарегистрированы'

    responseData = {
        'error': error
    }

    return JsonResponse(responseData)

def del_confirmed(request):
    print(request.POST)
    if request.user.is_authenticated:
        if request.user.is_superuser:

            customer = User.objects.filter(id = request.POST["id"])[0]
            order.objects.filter(customer = customer).filter(confirmed = True).delete()

            error = 'Все норм'
    else:
        error = 'Вы не зарегистрированы'

    responseData = {
        'error': error
    }

    return JsonResponse(responseData)
