from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tables
from .serializers import TableSerializer


class AddToken(viewsets.ModelViewSet):
    queryset = Tables.objects.all()
    serializer_class = TableSerializer
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        table = Tables.objects.filter(token=self.request.data['token'])
        if table.exists():
            return Response({'error': 'A table with this TOKEN already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        table = super().create(request, *args, **kwargs)
        return table


class ShowTables(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    http_method_names = ['get']

    def get_queryset(self):
        tables = Tables.objects.filter(cafe__name=self.kwargs['name'])
        return tables
