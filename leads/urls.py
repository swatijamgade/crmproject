from django.urls import path
from .views import LeadList, LeadDetail, LeadSourceListCreateView, LeadSourceDetail, LeadFollowUpAPI

urlpatterns = [
    path('lead/', LeadList.as_view, name='lead-list'),
    path('lead/<int:pk>/', LeadDetail.as_view, name='lead-detail'),
    path('lead-source/',LeadSourceListCreateView.as_view, name='lead-source-list'),
    path('lead-source/<int:pk>/',LeadSourceDetail.as_view, name='lead-source-detail'),
    path('lead-followup/', LeadFollowUpAPI.as_view, name='lead-followup-list'),
    path('lead-followup<int:pk>/',LeadFollowUpAPI.as_view, name='lead-followup-detail'),


]