from .views import DomainViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'domains', DomainViewSet, base_name='domain')
urlpatterns = router.urls
