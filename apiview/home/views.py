from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from home.serializers import StudentSerializer
from home.models import *
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    student_object = Student.objects.all()
    serializers = StudentSerializer(student_object,many=True)
    return Response({'id':int('1')+1,'Status':20,'Message':serializers.data})


@api_view(['POST','GET'])
def student_api(request):
    data = request.data
    serializers = StudentSerializer(data = request.data)
    if not serializers.is_valid():
        print(serializers.error)
        return Response({'status':403,'error':serializers.error})
    serializers.save()    
    return Response({'status':403,'error':serializers.data})


 
