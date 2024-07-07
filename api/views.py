from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TodoSerializer


class TodoApiView(APIView):
    serializer_class = TodoSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data": serializer.data, "message": "ToDo Created Successfully"},
                        status=status.HTTP_201_CREATED)
