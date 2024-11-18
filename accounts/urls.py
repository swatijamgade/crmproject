from django.urls import path
from .views import AcoountList, AccountDetail


urlpatterns = [
    path('account/', AcoountList.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
]