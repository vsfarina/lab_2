from django.urls import path
from .views import post_list, post_detail, post_new, post_edit, post_delete_confirm, add_comment
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Certifique-se de que essa URL está correta
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:post_pk>/comment/', add_comment, name='add_comment'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('post/<int:pk>/delete/confirm/', views.post_delete_confirm, name='post_delete_confirm'),
]
