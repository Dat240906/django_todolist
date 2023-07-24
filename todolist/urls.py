from django.urls import path
from .views import Show, Login, Index, DeleteItem


urlpatterns = [
    path('', Index.as_view(), name= 'index'),
    path('login-signup', Login.as_view(), name= 'login'),
    path('show', Show.as_view(), name= 'show'),
    path('delete-item/<int:item_id>', DeleteItem.as_view(), name='delete_item')
]