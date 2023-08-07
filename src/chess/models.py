from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.name
    
###pour mettre la migration :###

#python manage.py makemigrations
#python manage.py migrate


###pour remplir la base de données :###

#python manage.py shell
#>>> from chess.models import User
#>>> User.objects.create(name="Bob",age=20,email="bob.hello@gmail.com")


###fonctions utiles :###

#-récupérer le dernier objet de la base de données :
#>>> User.objects.last()

#-récupérer un objet par son id :
#>>> User.objects.get(id=1)

#-récupérer tous les objets:
#>>> User.objects.all()

# supprimer l'objet:
#>>> c.delete()     #en affectant c à l'objet récupéré

#accès aux attributs :
#>>> c.name
#>>> c.age         #en affectant c à l'objet récupéré
#>>> c.email

#sortir du shell:
#>>> exit()