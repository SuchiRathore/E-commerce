from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name="product-detail"),
    
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    path("cart/", views.showcart, name="showcart"),
    path("pluscart/",views.plus_cart,name="pluscart"),
    path("minuscart/",views.minus_cart,name="minuscart"),
    path("removecart/",views.remove_cart,name="removecart"),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
