from django.shortcuts import render

# Create your views here.
from app.serializers import *
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def school_jsondata(request):
    SOD=School.objects.all()
    JOD=SchoolSerializer(SOD,many=True)
    Jsondata=JOD.data
    return Response(Jsondata)
