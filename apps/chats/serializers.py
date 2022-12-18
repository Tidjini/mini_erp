from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.application.serialzers import ModelSerializerMixin
from .models import Utilisateur, Discussion, Message


class UtilisateurSerializer(ModelSerializerMixin):
    name = serializers.ReadOnlyField()
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
        model = Utilisateur
        exclude = ("password",)
        read_only_fields = ("id",)


class MessageSerializer(ModelSerializerMixin):

    receiver = serializers.SerializerMethodField()
    send_to = UtilisateurSerializer(source='sender', read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ("id",)

    def get_receiver(self, obj):
        receiver = obj.receiver
        return UtilisateurSerializer(receiver).data


class DiscussionSerializer(ModelSerializerMixin):

    participants_count = serializers.ReadOnlyField()
    other = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Discussion
        fields = "__all__"
        read_only_fields = ("id",)

    def get_other(self, obj):

        request = self.context['request']
        if request and hasattr(request, 'user'):
            other = obj.other(request.user)
            if other:
                return UtilisateurSerializer(other).data
        return None

    def get_last_message(self, obj):
        last = obj.last_message
        if last:
            return MessageSerializer(last).data
        return None


# todo custom this notification to be send with discussion item


class DiscussionNotificationSerializer(ModelSerializerMixin):

    class Meta:
        model = Discussion
        fields = "__all__"
        read_only_fields = ("id",)


# Todo switch to english in applications

class MessageNotificationSerializer(ModelSerializerMixin):

    receiver = serializers.SerializerMethodField()
    send_to = UtilisateurSerializer(source='sender', read_only=True)
    notif_discussion = serializers.SerializerMethodField()
    # room = DiscussionNotificationSerializer(
    #     source='discussion', read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ("id",)

    def get_receiver(self, obj):
        receiver = obj.receiver
        return UtilisateurSerializer(receiver).data

    def get_notif_discussion(self, obj):
        # here the other is the sender
        # for receiver perspect
        other = obj.discussion.other(obj.receiver)
        data = DiscussionNotificationSerializer(obj.discussion).data
        data['other'] = UtilisateurSerializer(other).data
        return data
