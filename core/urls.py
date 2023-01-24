from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('criar/', views.post_create, name='post_create'),

]