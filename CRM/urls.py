# First-party
from companies import views as companies_views
from employees import views as employees_views
from partnerships import views as partnerships_views

# Django
from django.contrib import admin
from django.urls import path, include

# Third-party
from rest_framework import routers

# URLs генерируются автоматически через router, это "магия" DRF
# Это самый упрощенный случай, можно использовать и более гибкий подход
router_companies = routers.DefaultRouter()
router_companies.register('companies', companies_views.CompanyViewSet)

router_employees = routers.DefaultRouter()
router_employees.register('employees', employees_views.EmployeeViewSet)

router_partnerships = routers.DefaultRouter()
router_partnerships.register('partnerships', partnerships_views.PartnershipViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # логирование в "browsable API"
    path('', include(router_companies.urls)), # register urls for companies
    path('', include(router_employees.urls)), # register urls for employees
    path('', include(router_partnerships.urls)), # register urls for partnerships
]
