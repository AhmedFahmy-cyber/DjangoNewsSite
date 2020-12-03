from django.urls import path 

from .views import home , all_news , detailnews ,all_category ,category


app_name = 'main'

urlpatterns = [
    path('', home , name = 'home'),
    path('allnews/', all_news , name = 'allnews'),
    path('detail/<int:id>', detailnews , name = 'detail'),
    path('all-category', all_category , name = 'all-category'),
    path('category/<int:id>', category , name = 'category'),
]
