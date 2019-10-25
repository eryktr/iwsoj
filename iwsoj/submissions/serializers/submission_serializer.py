from rest_framework import serializers

from submissions.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def create(self, validated_data) -> Submission:
        submission = Submission.objects.create(
            sourceCode=validated_data["sourceCode"],
            language=validated_data["language"]
        )
        return submission
