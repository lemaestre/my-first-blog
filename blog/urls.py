from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<slug>/remove/', views.post_remove, name='post_remove'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug>/unpublish/', views.post_unpublish, name='post_unpublish'),
    path('drafts/<slug>/', views.post_draft_detail, name='post_draft_detail'),
    path('drafts/<slug:slug>/edit/', views.draft_edit, name='draft_edit'),

]

