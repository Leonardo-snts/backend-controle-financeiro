# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, GastoViewSet, AdicionarPessoaView

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'gastos', GastoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('adicionar-pessoa/', AdicionarPessoaView.as_view(), name='adicionar-pessoa'),
]

# endpoints
# api/pessoas/
# api/adicionar-pessoa/
# api/gastos/
# api/upload-pdf/
