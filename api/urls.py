from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
 	path('widget-list/', views.widgetList, name="widget-list"),
	path('widget-create/', views.widgetCreate, name="widget-create"),
	path('widget-detail/<str:pk>/', views.widgetDetail, name="widget-detail"),
	path('widget-update/<str:pk>/', views.widgetUpdate, name="widget-update"),
	path('widget-delete/<str:pk>/', views.widgetDelete, name="widget-delete"),
]