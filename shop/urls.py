from django.urls import path

from . import views



# Product Urls
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('product_details/<slug>/', views.ProductDetail.as_view(), name='product_details'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove_single_from_cart/<slug>/', views.remove_single_from_cart, name='remove_single_from_cart'),
   
]
