from django.db import models

# Create your models here.
class Collection(models.Model):
    name=models.CharField(max_length=60)
    slug=models.SlugField()          #SlugField : A short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    
    default_name="_defaut"

    @classmethod
    def get_default(cls) -> "Collection":       
        collection, created = cls.objects.get_or_create(name="Defaut",slug=Collection.default_name)
        return collection           #pour créer une collection par defaut si elle n'existe déjà pas
    
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    description=models.CharField(max_length=500)       
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)       #on_delete spécifie ce qui se passe pour les taches si on supprime une collection (ici on supprime les taches associé à la collection)
    
    def __str__(self):
        return self.description

###pour mettre la migration :###

#python manage.py makemigrations
#python manage.py migrate


###pour remplir la base de données :###

#python manage.py shell
#>>> from tasks.models import Collection
#>>> Collection.objects.create(name="Defaut",slug="defaut")


###fonctions utiles :###

#-récupérer le dernier objet de la base de données :
#>>> Collection.objects.last()

#-récupérer un objet par son id :
#>>> Collection.objects.get(id=1)

#-récupérer tous les objets:
#>>> Collection.objects.all()

#-supprimer tous les objets:
#>>> Collection.objects.all().delete()

#-supprimer l'objet:
#>>> c.delete()     #en affectant c à l'objet récupéré

#-accès aux attributs :
#>>> c.name
#>>> c.slug         #en affectant c à l'objet récupéré

#-sortir du shell:
#>>> exit()