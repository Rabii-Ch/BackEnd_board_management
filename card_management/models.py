from django.db import models

class User(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200,blank=False, default='')
    roles = models.CharField(max_length=70, blank=False, default='')
    
    def __str__(self):
	    return self.username


class Card(models.Model):
    board_name= models.CharField(max_length=70, blank=False, default='')
    Board_type = models.CharField(max_length=70, blank=False, default='')
    STM32Family = models.CharField(max_length=70, blank=False, default='')
    reference = models.CharField(max_length=70, blank=False, default='')
    Status = models.CharField(max_length=70, blank=False, default='')
    Owner = models.CharField(max_length=70, blank=False, default='')
    Needed = models.CharField(max_length=70, blank=False, default='')
    Quantity = models.CharField(max_length=70, blank=False, default='')
    DHL_tracking = models.CharField(max_length=70, blank=False, default='')
    name_Reception = models.CharField(max_length=70, blank=False, default='')
    Date_reception = models.CharField(max_length=70, blank=False, default='')
    etat = models.BooleanField(default=False)
    
    def __str__(self):
	    return self.board_name

class Reservation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
