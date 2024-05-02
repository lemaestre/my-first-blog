from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new', views.create, name='new_post'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('post/<slug>/remove', views.post_remove, name='post_remove'),
    path('post/<slug>/publish', views.post_publish, name='post_publish'),
    path('post/<slug>/unpublish', views.post_unpublish, name='post_unpublish'),
    path('drafts/<slug>/', views.draft_detail, name='draft_detail'),
    path('drafts/<slug:slug>/edit', views.draft_edit, name='draft_edit'),
    path('category/<slug:slug>', views.category_posts, name='category_posts'),
    path('categories', views.category_list, name='category_list'),
    path('search', views.search_feature, name='search-view'),
    path('tag/<slug:slug>', views.tagged, name='tagged'),

]

