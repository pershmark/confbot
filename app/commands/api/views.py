from rest_framework import generics, status, mixins
from rest_framework.response import Response

from commands.api.serializers import APICommandSerializer, APICommandSerializerResponse
from commands.models import Command


class CommandView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Command.objects.all()
    serializer_class = APICommandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     serializer = APICommandSerializerResponse(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
