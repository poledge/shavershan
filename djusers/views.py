from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shavershan.models import feed, order
from django.contrib.auth.models import User


@login_required
def basket(request):
    if request.user.is_authenticated:

        user = request.user
        orders_array = order.objects.filter(customer = request.user).filter(confirmed = False)
        confirmed_orders_array = order.objects.filter(customer = request.user).filter(confirmed = True)
        
        check_user = "%s/seller/check/?user=%s" % (request.META['HTTP_HOST'], user.id)

        context = {
            'check_user': check_user,
            'orders_array': orders_array,
            'confirmed_orders_array': confirmed_orders_array
        }

    return render(request, "basket.html", context)


def home(request):
    user = request.user
    feedarray = feed.objects.all()

    return render(request, "home.html", {'user': user, 'feedarray': feedarray})
