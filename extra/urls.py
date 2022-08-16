from django.urls import path
from . import views

urlpatterns = [
	path('tag-list/', views.tag_list, name='tag_list'),
	path('tag-search/', views.tag_search, name='tag_search'),
]