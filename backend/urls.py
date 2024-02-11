from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from gerenciamento_estacionamento.views import ClienteViewSet, VeiculoViewSet, EstacionamentoViewSet, TarifaViewSet
from profiles.views import ProfileViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super().__init__()

    def get_lookup_regex(self, viewset, lookup_prefix=''):
        base_regex = super().get_lookup_regex(viewset, lookup_prefix)
        return fr'{base_regex}?'

router = OptionalSlashRouter()
router.register(r'Clientes', ClienteViewSet, basename='clientes')
router.register(r'Veiculos', VeiculoViewSet, basename='veiculos')
router.register(r'Estacionamentos', EstacionamentoViewSet, basename='estacionamentos')
router.register(r'Tarifas', TarifaViewSet, basename='tarifas')
router.register(r'Profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/token-refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Adiciona rotas específicas para cada ViewSet com barras finais opcionais
urlpatterns += [
    re_path(r'^api/Clientes/(?P<pk>\d+)/?$', ClienteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='clientes-detail'),
    re_path(r'^api/Veiculos/(?P<pk>\d+)/?$', VeiculoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='veiculos-detail'),
    re_path(r'^api/Estacionamentos/(?P<pk>\d+)/?$', EstacionamentoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='estacionamentos-detail'),
    re_path(r'^api/Tarifas/(?P<pk>\d+)/?$', TarifaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='tarifas-detail'),
    re_path(r'^api/Profiles/(?P<pk>\d+)/?$', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profiles-detail'),
]
