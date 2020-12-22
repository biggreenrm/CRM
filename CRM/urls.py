# First-party
from companies import views

# Django
from django.contrib import admin
from django.urls import path, include

# Third-party
from rest_framework import routers

# URLs генерируются автоматически через router, это "магия" DRF
# Это самый упрощенный случай, можно использовать и более гибкий подход
router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # логирование в "browsable API"
    path('', include(router.urls)),
]
