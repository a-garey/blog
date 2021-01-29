from django.urls import path 
from . import views

app_name = 'chirp_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pubs/', views.pubs, name = 'pubs'),
    path('blog/', views.blog, name = 'blog'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('post/<id>', views.post, name = 'post'),
]
