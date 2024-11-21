from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('maintance/', views.mentaince, name='mentaince'),
    path('feature/', views.feature, name='feature'),
    path('supplier/', views.supplier, name='supplier'),
    path('make_an_order/', views.make_an_order, name='make_an_order'),
    
]
