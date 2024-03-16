from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/unpublish/', views.post_unpublish, name='post_unpublish'),
    path('drafts/<pk>/draftfile/', views.post_draft_detail, name='post_draft_detail'),
    path('drafts/<int:pk>/edit/', views.draft_edit, name='draft_edit'),

]

