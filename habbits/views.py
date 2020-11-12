from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import habbit
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import habbitSerializer, HabbitUpdateSerializer


class HabbitListCreateView(ListCreateAPIView):
    queryset = habbit.objects.all()
    serializer_class = habbitSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        habbit = self.request.habbit
        serializer.save(habbit=habbit)


class HabbitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = habbit.objects.all()
    serializer_class = HabbitUpdateSerializer
    permission_class = [IsAuthenticated]
