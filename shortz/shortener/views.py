from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import URLEntrySerializer
from .models import URLEntry


@api_view(['POST'])
def shorten_url(request):
    serializer = URLEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def resolve_to_full_url(request, code=None):
    full_url = URLEntry.objects.get(code=code).url
    return redirect(full_url)
