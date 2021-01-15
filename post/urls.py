
from django.urls import path
from .views import postDetailView,postCreateView,postUpdateView
urlpatterns = [
    path('detail/<str:id>/',postDetailView,name='post-detail'),
    path('update/<str:id>',postUpdateView,name='post-update'),
    path('create/',postCreateView,name='post-create'),

]