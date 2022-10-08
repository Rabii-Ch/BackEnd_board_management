
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from card_management.models import User
from card_management.models import Card

from card_management.serializers import UserSerializer
from card_management.serializers import CardSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
import datetime


@api_view(['GET', 'POST', 'DELETE'])
def User_list(request):
    if request.method == 'GET':
        card_management = User.objects.all()
        
        username = request.GET.get('username', None)
        if username is not None:
            card_management = card_management.filter(user__icontains=username)
        
        card_management_serializer = UserSerializer(card_management, many=True)
        return JsonResponse(card_management_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse({'message': 'Email does exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} card_management were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE','POST'])
def user_detail(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data) 
 
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        user.delete() 
        card_management = User.objects.all()
        card_management_serializer = UserSerializer(card_management, many=True)
        return JsonResponse(card_management_serializer.data, safe=False)
@api_view(['POST']) 
def user_login(request):
    try: 
        body = JSONParser().parse(request)
        user = User.objects.get(email=body["email"],password=body["password"])
    except User.DoesNotExist: 
        return JsonResponse({'message': 'Incorrect email or password'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data)

    






@api_view(['GET', 'POST', 'DELETE'])
def Card_list(request):
    if request.method == 'GET':
        card_management = Card.objects.all()
        
        board_name = request.GET.get('board_name', None)
        if board_name is not None:
            card_management = card_management.filter(user__icontains=board_name)
        
        card_management_serializer = CardSerializer(card_management, many=True)
        return JsonResponse(card_management_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        Card_data = JSONParser().parse(request)
        Card_serializer = CardSerializer(data=Card_data)
        if Card_serializer.is_valid():
            Card_serializer.save()
            return JsonResponse(Card_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} card_management were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Card_detail(request, pk):
    try: 
        card = Card.objects.get(pk=pk) 
    except Card.DoesNotExist: 
        return JsonResponse({'message': 'The Card does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        Card_serializer = CardSerializer(card) 
        return JsonResponse(Card_serializer.data) 
 
    
    elif request.method == 'PUT': 
        card_data = JSONParser().parse(request) 
        Card_serializer = CardSerializer(card, data=card_data) 
        if Card_serializer.is_valid(): 
            Card_serializer.save() 
            return JsonResponse(Card_serializer.data) 
        return JsonResponse(Card_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        card.delete() 
        card_management = Card.objects.all()
        card_management_serializer = CardSerializer(card_management, many=True)

        return JsonResponse(card_management_serializer.data, safe=False)
    