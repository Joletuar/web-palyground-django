from django.db import models
from django.contrib.auth.models import User

#-------- Descripción d elas relaciones ----------

# -OneToOneField (1:1) 1 usuario 1 perfil
# -ForeignKeyField (1:N) 1 autor <- NEntradas
# -ManyToManyField (N:M) NEntradas <-> MCategorías

#-------------------------------------------------

# Create your models here.
class Profile(models.Model):
    
    # Vamos a crear un relación con otro modelo
    # Relación de 1 a 1
    # Solo puede haber un perfil por usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True, max_length=200)
