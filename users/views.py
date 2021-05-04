from django.shortcuts import render
from .serializers import LeaveSerializer,GetLeaveSerializer
from .models import Leave,GetLeave
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class GetLeaveViewSet(viewsets.ModelViewSet):
    queryset = GetLeave.objects.all()
    serializer_class = GetLeaveSerializer

    @action(detail=True,methods=['POST'])
    def put_leave(self,request,pk=None):
        if 'days' and 'user' in request.data:
            leave = Leave.objects.get(id=pk)
            user = request.data['user']
            response = {'Message' : 'Complete'}
            return Response(response,status=status.HTTP_200_OK)
        else :
            response = {'Message' : 'Please put days and user'}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

