from rest_framework import serializers

from submissions.models import Submission
from submissions.code_validator.code_validator import validate_code
from submissions.status import Status


class SubmissionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def create(self, validated_data) -> Submission:
        """
        :param validated_data: validated field of the submission (sourceCode, task, language)
        
        :return: model of the submission
        """
        sourceCode = validated_data['sourceCode']
        task = validated_data['task']
        language = validated_data["language"]
        validation_out = self._validate(sourceCode, language, task)
        status = validation_out[0]
        if status == Status.CE:
            error = validation_out[1]
        elif status == Status.WA:
            error = validation_out[1]
        else:
            error = None

        submission = Submission.objects.create(
            sourceCode=sourceCode,
            language=language,
            task=task,
            user=self._get_user(),
            status=status.value,
            error=error
        )
        return submission

    # extracted for mock
    def _validate(self, source_code, language, task):
        return validate_code(source_code, language, task)

    def _get_user(self):
        return self.context['request'].user
