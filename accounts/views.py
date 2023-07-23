from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.serializers import AccountSerializer,CustomAccountSerializer
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def register_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

from accounts.models import Account

@api_view(['POST'])
def login_account(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Account.objects.get(email=email)
        if user.password == password:
        
            return Response({'message': '登入成功'}, status=200)
        else:
     
            return Response({'message': '登入失敗'}, status=401)
    except Account.DoesNotExist:
   
        return Response({'message': '登入失敗'}, status=401)
    

from accounts.models import Account
from accounts.serializers import AccountSerializer

@api_view(['GET'])
def list_accounts(request):
    email = request.query_params.get('email')  
    if email:
        accounts = Account.objects.filter(email=email)
    else:
        accounts = Account.objects.all()
    serializer = CustomAccountSerializer(accounts, many=True)
    return Response(serializer.data, status=200)

from rest_framework_jwt.settings import api_settings


