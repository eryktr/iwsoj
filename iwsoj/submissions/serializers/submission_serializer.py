from rest_framework import serializers

from submissions.models import Submission
#from submissions.tester.tester import validate_code


class SubmissionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def create(self, validated_data) -> Submission:
        sourceCode = validated_data['sourceCode']
        task = validated_data['task']
        language = validated_data["language"]
        status = 0 #validate_code(sourceCode, language, task)
        submission = Submission.objects.create(
            sourceCode=sourceCode,
            language=language,
            task=task,
            user=self.context['request'].user,
            status=status
        )
        return submission
