from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Habbit
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import HabbitSerializer, HabbitUpdateSerializer


class HabbitView(APIView):
    def post(self, request):
        habbit = request.data.get('habbit')

        serializer = HabbitSerializer(data=habbit)
        if serializer.is_valid(raise_exception=True):
            habbit_saved = serializer.save()
        return Response({"success": "Habbit '{}' created successfully".format(habbit_saved.habbit_name)})


class HabbitListCreateView(ListCreateAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        habbit = self.request.habbit
        serializer.save(habbit=habbit)


class HabbitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitUpdateSerializer
    permission_class = [IsAuthenticated]
