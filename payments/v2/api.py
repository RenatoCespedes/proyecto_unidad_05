from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status, generics,filters
from .models import Payment_users,Service,Expired_payments
from .serializers import PaymentSerializer,ServiceSerializer, ExpiredSerializer
import math
from .pagination import StandardPagination
from django.contrib.auth.models import Permission
# from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView, status
from rest_framework import viewsets
from django.http import Http404
from users.models import User
from rest_framework.generics import get_object_or_404
from .permisos import UserPermission, UserPaymentPermission,UserExpiredPermission

#------------------- payment--------------------------------#
class ApiPayment(viewsets.ModelViewSet):
    queryset=Payment_users.objects.all()
    pagination_class=StandardPagination
    #permission_classes = [UserPaymentPermission]
   # filter_backends = [filters.OrderingFilter]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('Payment_date','Expiration_date')

    def get_serializer_class(self):
        return PaymentSerializer
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        # permiso=Permission.objects.filter(user=request.user.id)
        print("---------")
        print(request.user.is_superuser)
        print(request.user.is_active)
        print(request.method)
        # if():
        if page is not None:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(page, many=True,context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Payment_users.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        print(request.method)
        serializer = PaymentSerializer(todo,context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        if isinstance(request.data, list):
            serializer = PaymentSerializer(data=request.data, many=True,context={'request': request})
        else:
            serializer = PaymentSerializer(data=request.data,context={'request': request})
        date_payment=datetime.strptime(request.data['Payment_date'], '%Y-%m-%d')
        exp_date=datetime.strptime(request.data['Expiration_date'], '%Y-%m-%d')
        
        
        if serializer.is_valid():
            serializer.save()
            if(date_payment > exp_date):
                result=date_payment - exp_date
                result=result.days*5.4    
                x=Expired_payments.objects.create(Payment_user_id=Payment_users.objects.last(),Penalty_fee_amount=result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Payment_users.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(todo, data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def partial_update(self, request, pk=None):
        queryset = Payment_users.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(todo, data=request.data, partial=True,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Payment_users.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#------------------- service--------------------------------#
class ApiService(viewsets.ModelViewSet):
    queryset=Service.objects.all()
    pagination_class=StandardPagination
    #permission_classes=[UserPermission]
    # http_method_names = ['get']
    def get_serializer_class(self):
        return ServiceSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(page, many=True,context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(todo,context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        if isinstance(request.data, list):
            serializer = ServiceSerializer(data=request.data, many=True,context={'request': request})
        else:
            serializer = ServiceSerializer(data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Service.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(todo, data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Service.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(todo, data=request.data, partial=True,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Service.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#------------------- expired--------------------------------#
class ApiExpired(viewsets.ModelViewSet):
    queryset=Expired_payments.objects.all()
    pagination_class=StandardPagination
    #permission_classes=[UserExpiredPermission]
    http_method_names = ['get','post']
    def get_serializer_class(self):
        return ExpiredSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(page, many=True,context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Expired_payments.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ExpiredSerializer(todo,context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        if isinstance(request.data, list):
            serializer = ExpiredSerializer(data=request.data, many=True,context={'request': request})
        else:
            serializer = ExpiredSerializer(data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Expired_payments.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ExpiredSerializer(todo, data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = Expired_payments.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = ExpiredSerializer(todo, data=request.data, partial=True,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Expired_payments.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)