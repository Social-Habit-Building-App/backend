from rest_framework import serializers
from .models import Habbit


class HabbitSerializer(serializers.ModelSerializer):
    habbit = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Habbit
        fields = "__all__"

class HabbitUpdateSerializer(serializers.ModelSerializer):
    habbit = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Habbit
        exclude = ('user', )