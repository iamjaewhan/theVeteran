from django.db import models
from django.utils import timezone
from accounts.models import User, Host

# Create your models here.
class Game(models.Model):
    host = models.ForeignKey('accounts.Host', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    numOfRec = models.IntegerField(null=False, default=5)
    
    def is_Progressed(self):
        if self.start_datetime > timezone.localtime():
            return False
        else:
            return True
        
    def get_unprogressed():
        games = list(filter(lambda x:x.is_Progressed(), Game.objects.all()))
        return games
        
    
class Game_Participants(models.Model):
    game = models.ForeignKey(Game, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   

    class Meta:
        unique_together = (('game','user'))
    
    def get_participants(self):
        return len(Objects.filter(game=self.game))
        
        
class Game_numOfP(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    numOfP = models.IntegerField()