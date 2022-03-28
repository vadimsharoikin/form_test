from django.urls import path
from .import views


urlpatterns = [
	path('',views.MyFormView.as_view(),name='main'),
	path('data/',views.DataFormView.as_view(),name='data')
	
]