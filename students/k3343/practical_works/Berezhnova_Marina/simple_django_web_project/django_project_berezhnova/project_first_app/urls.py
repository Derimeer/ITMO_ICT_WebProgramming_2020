from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:driver_id>', views.get_driver),
        path('auto/', views.CarView.as_view()),
        path('owners/', views.get_drivers),
        path('owner/new/', views.get_driver_form),
        path('auto/new/', views.GetAutoForm.as_view(success_url="/auto/new/")),
]
