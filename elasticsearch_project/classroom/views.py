from msilib.schema import Class
from django.http import Http404
from django.shortcuts import render

from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Classroom
from .serializers import ClassroomSerializer

# Create your views here.
class GetCreateClassroom(APIView):

    def get_classroom(self, pk):
        try:
            return Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Http404 
        
    def get(self, request, id):
        qs = self.get_classroom(id)
        serialized_data = ClassroomSerializer(qs)

        return Response(serialized_data.data, status=status.HTTP_200_OK)


class ClassroomListView(APIView, LimitOffsetPagination):
    # LimitOffsetPagination is defined in settings.py, hence one page wil return 5 items
    def get(self, request):
        qs = Classroom.objects.all()
        serialized_data = ClassroomSerializer(qs, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
