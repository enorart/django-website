from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.text import slugify       #pour créer un slug à partir d'un nom

from tasks.models import Collection, Task      #on importe la BD Collection


# Create your views here.
def index(request):
    
    context={}
     
    collection_slug=request.GET.get("collection")        #on récupère le slug de la collection dans l'url
    
    if collection_slug:     #si le slug existe
        collection=get_object_or_404(Collection, slug=collection_slug)     
    else:
        collection=Collection.get_default()     #sinon on récupère la collection par défaut
        return redirect(f"{reverse('tasks-index')}?collection=_defaut")        #on redirige vers la page d'accueil avec le slug de la collection par défaut 
    context["collections"]=Collection.objects.order_by("slug")        #on récupère toutes les collections et on les classes par slug (ordre alphabetique)
    context["collection"]=collection
    context["tasks"]=collection.task_set.order_by("description")       #on récupère toutes les taches de la collection et on les classes par description (ordre alphabetique)
    
    return render(request, 'tasks/index.html',context=context)          #django trouve automatiquement les fichiers templates


def add_collection(request):
    
    collection_name= request.POST.get("collection-name")
    if collection_name=="":
        return HttpResponse("Le nom de la collection ne peut pas être vide", status=409)        #400 : bad request, on renvoie un message d'erreur
    if slugify(collection_name)=="defaut":
        return HttpResponse("Une collection ne peut pas avoir le nom 'defaut'", status=409)        #400 : bad request, on renvoie un message d'erreur
    
    collection, created=Collection.objects.get_or_create(slug=slugify(collection_name))     #get_or_create revoie un tuple avec (object, created)
    if not created:           #si la collection existe déjà, on ne veut pas de doublon
        return HttpResponse("La collection existe déjà", status=409)        #409 : conflict, on renvoie un message d'erreur
    elif created:       #si la collection n'existe pas déjà, on rajoute son nom (on fait la vérification de doublon par les slug pour éviter des problèmes après)
        collection.name=collection_name
        collection.save()
    
    return render(request, 'tasks/collections.html',context={"collection":collection})          


def add_task(request): 
    
    collection = get_object_or_404(Collection, slug=request.POST.get("collection"))     #on récupère la collection par son slug (unique grâce au vérification qu'on a fait), si elle n'existe pas on renvoie une erreur 404
    description = request.POST.get("task-description")
    
    if description=="":
        return HttpResponse("La description de la tache ne peut pas être vide", status=409) 
    
    task=Task.objects.create(description=description, collection=collection)
    
    return render(request, 'tasks/task.html',context={"task":task})         


def delete_task(request, task_pk):
    
    task=get_object_or_404(Task,pk=task_pk)
    task.delete()

    return HttpResponse("")     #car on veut enlever l'element


def get_task(request, collection_slug):
    
    collection=get_object_or_404(Collection, slug=collection_slug)     #on récupère la collection par son slug (unique grâce au vérification qu'on a fait), si elle n'existe pas on renvoie une erreur 404   
    tasks = collection.task_set.order_by("description")       
    
    return render(request, 'tasks/tasks.html',context={"tasks":tasks, "collection":collection})          #django trouve automatiquement les fichiers templates


def delete_collection(request, collection_slug):
        
    collection=get_object_or_404(Collection,slug=collection_slug)
    collection.delete()
        
    return redirect('tasks-index')         #on redirige vers la page d'accueil