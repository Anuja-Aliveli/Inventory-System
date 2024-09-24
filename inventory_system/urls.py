"""
URL configuration for inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.login import user_login
from authentication.register import user_registration
from products.views import add_product, get_project_details, product_details, update_product_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_registration),
    path('login/', user_login),
    path('items/', add_product),
    path('items/<str:item_id>', product_details)
]
