from rest_framework import serializers 
from card_management.models import User
from card_management.models import Card
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'password',
                  'roles')
        extra_kwargs = {'password': {'write_only': True}}
               



class CardSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Card
        fields = ('id',
                   'board_name',
                   'Board_type',
                   'STM32Family',
                   'reference', 
                   'Status', 
                   'Owner', 
                   'Needed',
                   'Quantity', 
                   'DHL_tracking', 
                   'name_Reception', 
                   'Date_reception',
                   'etat' )



                   