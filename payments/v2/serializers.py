from rest_framework import serializers
from .models import Payment_users,Service,Expired_payments

class PaymentSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name= 'pay-detail',
        lookup_field='pk'
    )
    # url=serializers.URLField()
    class Meta:
        model = Payment_users   
        fields = ('url','id','user_id','service_id','Amount','Payment_date','Expiration_date')
        # '__all__'
        
        # read_only_fields = '__all__',


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Service
        fields= '__all__'
        # exclude=['url']
        # read_only_fields = '__all__',


class ExpiredSerializer(serializers.ModelSerializer):
    class Meta:
        model= Expired_payments
        fields= '__all__'
        # read_only_fields = '__all__',