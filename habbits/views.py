from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Habbit
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import HabbitSerializer, HabbitUpdateSerializer


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
