from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('store/', include('apps.store.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
]
