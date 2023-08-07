# django-website
Creating my first website using django web framework, HTMX for the backend and bootstrap 5 for the frontend.

<br> _**🚧 WORK IN PROGRESS. The current version come with a little web application for to-do-list. 
It's a very simple application but it allowed me to familiarize myself with the django framework for the first time. 
It also come with a little home page which indicates the current date and time.
I plan to make a small chess game available on a browser like chess.com but in a cheap version ha ha !**_ 🚧 <br>

<br> _**😓 ️Sorry for my bad English, it's not my native language. I might do an English translation if many of you ask for it. The actual version is in French, but it's not very important to understand the code 😓**_ <br>

This repository contains the folowing contents.

* The main django project (src folder)
* In the django project, 2 applications (tasks for the to-do-list web application, and chess for the future (WORK IN PROGRESS) chess web application)
* requirements.txt for the requirements

# Requirements
* asgiref==3.7.2 or Later
* Django==4.2.3 or Later
* sqlparse==0.4.4 or Later
* tzdata==2023.3 or Later

You can do this command : <pre>pip install -r requirements.txt</pre> to install the libraries more easily 

# Demo 
1/ You need to go in the src folder in a command prompt. 
💡 Tip : open the project in your Python environment (for example VScode or Pycharm), go in the powershell and type : 
<pre> cd src</pre> 
to access the folder 💡

2/ Start running the local server with django 
<pre> python manage.py runserver</pre>

3/ Open the page in your browser

# Directory 

<pre> 
├─src
│  └─ chess
│  └─  Site
│  └─  tasks
│  │ db.sqlite3
│  │ manage.py 
│ 
│ requirements.txt
 </pre> 

### chess 

The futur chess web application
 🚧 WORK IN PROGRESS 🚧

 ### tasks

 A simple to-do-list web application.
 You can add collections and in these collections you can add tasks
 For example, you can add a collection named "grocery" and a task like "buy bread" 🥖
 You can also remove collections and tasks

 See the demo video below :

https://github.com/enorart/django-website/assets/135878234/f1dbef08-aeee-44ba-8b86-743d140a606f

 ### Site 

 A simple index view, which indicates the current date and time.

 <img width="1279" alt="image" src="https://github.com/enorart/django-website/assets/135878234/1adb1033-45c8-439f-ba4b-a5800c9d53cd">

# To do

* Chess application, to play chess on a the computer like chess.com but cheap haha
* Link to navigate the site, for now, you have to access the page manually by changing the url. For example, to access the to-do-list web application you need to type /tasks after the main root of the url

# Reference 

 * [Django](https://www.djangoproject.com/)
 * [HTMX](https://htmx.org/)
 * [Bootstrap](https://getbootstrap.com/)

# Author
Eno [https://github.com/enorart](https://github.com/enorart)

   

 





