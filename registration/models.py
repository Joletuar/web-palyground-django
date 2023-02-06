from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver # Corresponde a un decorador
from django.db.models.signals import post_save # Importamos la señal con la que decoraremos nuestro método

#-------- Descripción d elas relaciones ----------

# -OneToOneField (1:1) 1 usuario 1 perfil
# -ForeignKeyField (1:N) 1 autor <- NEntradas
# -ManyToManyField (N:M) NEntradas <-> MCategorías

#-------------------------------------------------

# Este método permite eliminar un avatar luego de de que se suba otra imagen
def custom_upload_to(instance, filename):
    # Recuperamos la antigua instancia
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profile/"+filename


# Create your models here.
class Profile(models.Model):
    
    # Vamos a crear un relación con otro modelo
    # Relación de 1 a 1
    # Solo puede haber un perfil por usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True, max_length=200)


# Vamos a crear nuestra propia señal

# Le pasamos el tipo de la señal que queremos configurar. Tambien le podemos pasar el modelo a usar
# pre_save
# post_save
# pre_delete
# post_delete

# Para nuestro caso necesitamos que el usuario exista, por lo cual usaremos post_save
@receiver(post_save, sender=User)
def ensure_profile_exists(sender,instance, **kargs):
    
    # Verificamos si dentro del diccionario de kargs se encuentra la variable "created", y devolvemos por defecto false si no existe dicha entrada
    if kargs.get('created', False):
        # No vamos a asegurar de crear una instancia de perfil si esta no existe
        Profile.objects.get_or_create(user=instance)
    

