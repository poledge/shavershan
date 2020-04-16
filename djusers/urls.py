from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

from accounts.views import login_view, register_view, logout_view
from api.views import *
from seller.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('basket/', basket),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('api/add_order/', add_order),
    path('api/del_order/', del_order),
    path('api/confirm_all/', confirm_all),
    path('api/update_order/', update_order),
    path('api/get_orders_count/', get_orders_count),
    path('seller/check/', check)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
