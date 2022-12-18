from rest_framework import serializers

from apps.application.serialzers import ModelSerializerMixin
from apps.general.serializers import ProfileSerializer
from .models import Discussion, Message


class MessageSerializer(ModelSerializerMixin):

    receiver = serializers.SerializerMethodField()
    send_to = ProfileSerializer(source='sender', read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ("id",)

    def get_receiver(self, obj):
        receiver = obj.receiver
        return ProfileSerializer(receiver).data


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
                return ProfileSerializer(other).data
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
    send_to = ProfileSerializer(source='sender', read_only=True)
    notif_discussion = serializers.SerializerMethodField()
    # room = DiscussionNotificationSerializer(
    #     source='discussion', read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ("id",)

    def get_receiver(self, obj):
        receiver = obj.receiver
        return ProfileSerializer(receiver).data

    def get_notif_discussion(self, obj):
        # here the other is the sender
        # for receiver perspect
        other = obj.discussion.other(obj.receiver)
        data = DiscussionNotificationSerializer(obj.discussion).data
        data['other'] = ProfileSerializer(other).data
        return data
