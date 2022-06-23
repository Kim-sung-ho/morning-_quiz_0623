from unicodedata import category
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from item.serializers import CategorySerializer, ItemSerializer

# Create your views here.


class itemView(APIView):
    def get(self, request):
        category = request.GET.get('category', '')
        return Response(CategorySerializer(category).data, status.HTTP_200_OK)

    def post(self, request):
        item = ItemSerializer(data=request.data)
        item.is_valid(raise_exception=True)
        item.save()
        return Response(item.data, status.HTTP_200_OK)


class itemOrderView(APIView):
    # validate
    def get(self, request):
        return Response({"message": "ok!"})
    # creat

    def post(self, request):
        return Response({"message": "ok!"})
    # update

    def put(self, request, id):
        return Response({"message": "ok!"})
