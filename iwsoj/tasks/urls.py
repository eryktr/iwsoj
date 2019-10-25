from rest_framework import routers
from tasks.api import TaskViewSet


router = routers.DefaultRouter()
router.register("", TaskViewSet, "")

urlpatterns = router.urls
