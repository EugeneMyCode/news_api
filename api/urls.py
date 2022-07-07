from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('createnews/', views.add_news, name='add-news'),
    path('news/<int:pk>/', views.exactly_news, name="exactly-news"),
    path('news/', views.view_news, name='view_news'),
    path('news/<int:pk>/update', views.update_news, name='update-news'),
    path('news/<int:pk>/delete/', views.delete_news, name='delete-news'),
    path('createtypenews/', views.add_typenews, name='add-typenews'),
    path('typenews/<int:pk>/', views.exactly_typenews, name="exactly-typenews"),
    path('typenews/', views.view_typenews, name='view_typenews'),
    path('typenews/<int:pk>/update', views.update_typenews, name='update-typenews'),
    path('typenews/<int:pk>/delete/', views.delete_typenews, name='delete-typenews'),
]