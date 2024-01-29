from rest_framework import serializers
from job.models import Job,Category,Apply

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields  = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = ['name',]
        
class ApplySerializers(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields  = '__all__'
        

