from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer


# Handles: GET all jobs, POST a new job
@api_view(['GET', 'POST'])
def job_list(request):

    if request.method == 'GET':
        jobs = Job.objects.all().order_by('-id')    #Get all jobs, newest first
        serializer = JobSerializer(jobs, many=True)   #Convert to JSON
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)   #Take data sent from React
        if serializer.is_valid():                          #Validate it
            serializer.save()                               #Save to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Handles: GET one job, PUT (edit), DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)        #Find job by its ID
    except Job.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)   #Update existing job
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        job.delete()
        return Response({'message': 'Job deleted'}, status=status.HTTP_204_NO_CONTENT)