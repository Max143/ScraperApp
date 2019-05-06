from django.urls import path
from . import views

urlpatterns = [
	path('scraper/', views.Scraper, name='scraper'),
    path('scraper/bloglist/', views.BlogList, name='engine'),
    
    
]
