from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from .serializers import ToDoSerializer
from .models import ToDo
from django.http import HttpResponse


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(user=self.kwargs.get('user', None))

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = self.kwargs.get('user', None)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def APIIncrement(request):
    cafe = ToDo.objects.get(name="Hollys Coffee Daegu")
    cafe.description = int(cafe.description) + 1
    cafe.save()
    return HttpResponse(status=200)

def APIDecrement(request):
    cafe = ToDo.objects.get(name="Hollys Coffee Daegu")
    cafe.description = int(cafe.description) - 1
    cafe.save()
    return HttpResponse(status=200)