from rest_framework import status
from rest_framework.response import Response
from rest_framework .views import APIView
from django.shortcuts import get_object_or_404
from .models import Lead, LeadSource, LeadFollowUp
from .serializers import LeadSerializer, LeadSourceSerializer, LeadAssignSerilaizer, LeadFolloUpSerializer

class LeadList(APIView):
    def get(self, request):
        lead = Lead.objects.all()
        serializer = LeadSerializer(lead, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class LeadDetail(APIView):
    def get(self, request, pk):
        try:
            lead = Lead.objects.get(pk=pk)
            serializer = LeadSerializer(lead)
            return Response(serializer.data)
        except Lead.DoesNotExit:
             return Response ({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            lead = Lead.objects.get(pk=pk)
            serializer = LeadSerializer(lead, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Lead.DoesNotExit:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            lead = Lead.objects.get(pk)
            lead.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Lead.DoesNotExit:
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)


class LeadSourceListCreateView(APIView):

    def get(self, request):
        lead_source = LeadSource.objetcs.all()
        serializer = LeadSerializer(lead_source, many=True)
        return Response({'detail': 'Not Found'}, status= status.HTTP_200_OK)

    def post(self, request):
        serializer = LeadSourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeadSourceDetail(APIView):

    def get(self, request, pk):
        try:
            # Retrieve the LeadSource object using primary key (pk)
            lead_source = LeadSource.objects.get(pk=pk)
            serializer = LeadSourceSerializer(lead_source)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LeadSource.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Catch any other unexpected errors
            return Response({'detail': 'unexpected error occur'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
         try:
             lead_source = LeadSource.objects.get(pk=pk)
             serializer = LeadSerializer(lead_source, data=request.data)
             if serializer.is_valid:
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_200_OK)
         except LeadSource.DoesNotExits:
             return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
         except Exception :
             return Response({'detail': 'unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            lead_source = LeadSource.objects.get(pk=pk)
            lead_source.delete()  # Delete the LeadSource object
            return Response({'detail': 'Lead Source deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except LeadSource.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception :
             return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeadFollowUpAPI(APIView):
    """
    API View for handling Lead Follow-Up retrieval and creation.
    """

    def get(self, request, pk):
        """
        Retrieve all lead follow-ups.
        """
        # Query all follow-ups
        lead_followups = LeadFollowUp.objects.all()
        # Serialize the data
        serializer = LeadFolloUpSerializer(lead_followups, many=True)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """
        Create a new lead follow-up.
        """
        # Deserialize the data
        serializer = LeadFolloUpSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new follow-up to the database
            serializer.save()
            return Response({'deatil': 'Followup created sussfully'}, status=status.HTTP_201_CREATED)
        # Return validation errors if invalid
        return Response({'Error': 'errors'}, status=status.HTTP_400_BAD_REQUEST)




