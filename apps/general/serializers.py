from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from apps.application.serialzers import ModelSerializerMixin
from . import models


class TvaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tva
        fields = '__all__'
        read_only_fields = 'id',


class LocalisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Localisation
        fields = '__all__'
        read_only_fields = 'id',


class ProfileSerializer(ModelSerializerMixin):
    name = serializers.ReadOnlyField()
    task_count = serializers.ReadOnlyField()
    distance = serializers.ReadOnlyField()
    localisation = LocalisationSerializer(read_only=True)

    password_one = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    password_two = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    def save(self, **kwargs):
        pwd_one, pwd_two = [
            value
            for key, value in self.validated_data.items()
            if key in ("password_one", "password_two")
        ]
        # check passwords confromity
        if pwd_one != pwd_two:
            raise ValidationError("Passwords not matched, retry again")

        self.clean_validate_data()
        self._validated_data.update(password=pwd_one)

        try:
            return super().save(**kwargs)
        except ValueError as e:
            raise ValidationError(f'Exception du to: {e}')

    class Meta:
        model = models.Profile
        exclude = ("password",)
        read_only_fields = ("id",)
