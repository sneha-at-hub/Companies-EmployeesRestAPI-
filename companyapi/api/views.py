from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework import status
import logging
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

logger = logging.getLogger(__name__)

# Create your views here.

# ModelViewSet gives all the methods like create, update, etc.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    # companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = get_object_or_404(Company, pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            logger.info(f"Method get executed for employees of company {pk}")
            return Response(emps_serializer.data)
        except Company.DoesNotExist:
            logger.error(f"Company with id {pk} does not exist.")
            return Response({'message': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return Response({'message': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
