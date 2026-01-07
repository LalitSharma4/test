from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User, Item
from api.serializers import UserSerializer, ItemSerializer


class UsersListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ItemsListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)