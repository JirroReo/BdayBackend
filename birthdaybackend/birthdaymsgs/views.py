# views.py
from rest_framework import viewsets

from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.filter(is_visible=True).order_by('-date_added')
    serializer_class = MessageSerializer