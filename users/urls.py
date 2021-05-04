from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import LeaveViewSet,GetLeaveViewSet

router = routers.DefaultRouter()
router.register('leave',LeaveViewSet)
router.register('get_leave',GetLeaveViewSet)

urlpatterns = [
    path('',include(router.urls))
]