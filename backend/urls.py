from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from gerenciamento_estacionamento.views import  ClienteViewSet, VeiculoViewSet, EstacionamentoViewSet, TarifaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'Clientes', ClienteViewSet, basename='clientes')
router.register(r'Veiculos', VeiculoViewSet, basename='veiculos')
router.register(r'Estacionamentos', EstacionamentoViewSet, basename='estacionamentos')
router.register(r'Tarifas', TarifaViewSet, basename='tarifas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path("api/", include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]