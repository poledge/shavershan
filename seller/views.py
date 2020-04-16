from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shavershan.models import feed, order
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound


@login_required
def check(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:

            customer = User.objects.filter(id = request.GET["user"])[0]
            confirmed_orders_array = order.objects.filter(customer = customer).filter(confirmed = True)
            
            final_cost = 0
            for i in confirmed_orders_array:
                final_cost = final_cost + i.feed.cost * i.count

            context = {
                'final_cost': final_cost,
                'customer': customer, 
                'confirmed_orders_array': confirmed_orders_array
            }
            return render(request, "check.html", context)
        else:
            return HttpResponseNotFound('Вы не являетесь администратором')



