# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, AdicionarPessoaView, ProcessFileView, ProcessedDataViewSet, TotalGastosPessoaView

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'gastos', ProcessedDataViewSet)

urlpatterns = [  
    path('', include(router.urls)),
    path('process-file/', ProcessFileView.as_view(), name='process_file'),
    path('adicionar-pessoa/', AdicionarPessoaView.as_view(), name='adicionar-pessoa'),
    path('total-gastos/<int:pessoa_id>/', TotalGastosPessoaView.as_view(), name='total-gastos'),
]

# endpoints

# api/pessoas/
# api/adicionar-pessoa/
# api/gastos/
# api/upload-pdf/
