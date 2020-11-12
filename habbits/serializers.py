from rest_framework import serializers
from .models import habbit


class habbitSerializer(serializers.ModelSerializer):
    habbit = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = habbit
        fields = "__all__"

class HabbitUpdateSerializer(serializers.ModelSerializer):
    habbit = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = habbit
        exclude = ('user', )