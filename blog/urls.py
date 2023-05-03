from django.urls import path
from .views import *

urlpatterns = [
    path('list/', PostViewSet.as_view({'get':'list'})),
    path('posts/', PostViewSet.as_view({'post':'create'})),
    path('repl/', CommentViewSet.as_view({'post':'create'})),
    path('posts/<int:pk>/', PostViewSet.as_view({'get':'retrieve'})),
]