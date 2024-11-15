from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer



@api_view(['POST'])
def add_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_contact(request, number):
    try:
        contact = Contact.objects.get(number=number)

    except Contact.DoesNotExist:
        return Response({'Error: Contact not found'}, status = status.HTTP_404_NOT_FOUND)

    serializer = ContactSerializer(contact)
    return Response(serializer.data, status=status.HTTP_200_OK)