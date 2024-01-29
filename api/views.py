from django.shortcuts import render
from django.http import Http404, JsonResponse
from .serializers import JobSerializers,CategorySerializers,ApplySerializers
from job.models import Job,Category,Apply
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins,viewsets
from rest_framework.views import  APIView
# Create your views here.


#  no rest framework no api Just json data
def no_rest(request):
    jobs = Job.objects.all()
    response = {
        'jobs': list(jobs.values('title','salary'))
    }
    return JsonResponse(response)

# Get_list 
# Post 
# Get_item
# Put 
# Delete

@api_view(['GET','POST'])
def FBV_list(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializers(jobs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])   
def FBV_pk(request,pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        raise ValueError('Does not Exist')  
    if request.method == "GET":
        serializer = JobSerializers(job) 
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = JobSerializers(job,data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CBV_list(APIView)  :
    def get(self,request):
        jobs = Job.objects.all()
        serializer = JobSerializers(jobs,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)  
class CBV_pk(APIView):
    def get_object(self,pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        job = self.get_object(pk) 
        serializer = JobSerializers(job)
        return Response(serializer.data)
    def put(self,request,pk):
        job = self.get_object(pk)
        serializer = JobSerializers(job,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
       
class Mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)   
class Mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)  

class Generic_list(generics.ListCreateAPIView) :     
    queryset = Job.objects.all()
    serializer_class = JobSerializers
class Generic_pk(generics.RetrieveUpdateDestroyAPIView) :     
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class viewsetsjobs(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializers