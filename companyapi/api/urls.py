from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet

# Create a router instance
router = routers.DefaultRouter()

# Register CompanyViewSet with the router
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)


# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
