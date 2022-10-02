from rest_framework import serializers
from . import models

class RegisteredParthersSerilizer(serializers.ModelSerializer):

    class Meta:
        model = models.RegisteredParthers
        fields ='__all__'




class ContactUsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactUs
        fields ='__all__'


# 