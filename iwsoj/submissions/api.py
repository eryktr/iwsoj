from submissions.models import Submission
from rest_framework import viewsets, permissions
from .serializers.submission_serializer import SubmissionSerializer
from users.api import AuthUserToken


class SubmissionViewSet(viewsets.ModelViewSet):
    authentication_classes = [
        AuthUserToken
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)
