from rest_framework import routers
from submissions.api import SubmissionViewSet


router = routers.DefaultRouter()
router.register("", SubmissionViewSet, "")

urlpatterns = router.urls
