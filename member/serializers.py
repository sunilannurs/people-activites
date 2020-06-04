from rest_framework import serializers
from .models import ActivityPeriod, User


class ActivityPeriodSerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

    def get_start_time(self, obj):
        format = '%Y-%m-%d %H:%M %p'
        return obj.start_time.strftime(format)
    
    def get_end_time(self, obj):
        format = '%Y-%m-%d %H:%M %p'
        return obj.end_time.strftime(format)


class UserSerializer(serializers.ModelSerializer):
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    def get_activity_periods(self, user_obj):
        return ActivityPeriodSerializer(user_obj.activity_periods.all(), many=True).data