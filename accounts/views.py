from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer

class AcoountList(APIView):

     # list all account or create account
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

     # for detail view
class AccountDetail(APIView):

    def get(self, request, pk):
      try:
          account = Account.objects.get(pk=pk)
          serializer = AccountSerializer(account)
          return Response(serializer.data)
      except Account.DoesNotExit:
          return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def put(sel, request, pk):
          try:
              account = Account.objects.get(pk=pk)
              serializer = AccountSerializer(account, data=request.data)
              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          except Account.DoesNotExit:
              return Response({'deatil': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            account = Account.objects.get(pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExit:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


