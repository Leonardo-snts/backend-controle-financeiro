# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, AdicionarPessoaView, ProcessFileView, ProcessedDataViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'gastos', ProcessedDataViewSet)

urlpatterns = [  
    path('', include(router.urls)),
    path('process-file/', ProcessFileView.as_view(), name='process_file'),
    path('adicionar-pessoa/', AdicionarPessoaView.as_view(), name='adicionar-pessoa'),
]

# endpoints

# api/pessoas/
# api/adicionar-pessoa/
# api/gastos/
# api/upload-pdf/
