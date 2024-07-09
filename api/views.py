from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TodoSerializer
from base.models import ToDo


class TodoApiView(APIView):
    serializer_class = TodoSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data": serializer.data, "message": "ToDo Created Successfully"},
                        status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = ToDo.objects.all().order_by("-id")
        serializer = TodoSerializer(queryset, many=True)
        return Response({"data": serializer.data, "message": "ToDo List Success"}, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"message": "ToDo Not Found"}, status=status.HTTP_400_BAD_REQUEST)

        if todo:
            serializer = TodoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({"data": serializer.data, "message": "ToDo Update Success"}, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"message": "ToDo Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        todo.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
