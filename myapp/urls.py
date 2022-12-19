from django.urls import path

from myapp.views import index, login_view, logout_view, create_new_hit_view, detail_hit_view, list_hitmen, hitman_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('hit/new/', create_new_hit_view, name='hit_new'),
    path('hit/<int:pk>/', detail_hit_view, name='hit_detail'),
    path('hitmen/', list_hitmen, name='list_hitmen'),
    path('hitmen/<int:pk>/', hitman_detail, name='hitman_detail'),
    path('', index, name='home'),
]