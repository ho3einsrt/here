from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Cafes
from .serializers import CafeSerializer


class AddUpdateCafe(viewsets.ModelViewSet):
    queryset = Cafes.objects.all()
    serializer_class = CafeSerializer
    http_method_names = ('get', 'post', 'put')

    def create(self, request, *args, **kwargs):
        cafe = Cafes.objects.filter(name=self.request.data['name'])
        if cafe.exists():
            return Response({'error': 'A cafe with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST) # or 406?
        cafe = super().create(request, *args, **kwargs)
        return cafe
