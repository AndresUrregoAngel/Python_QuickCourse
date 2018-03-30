### First deployment 

##### This practical session was based in this [django tutorial](https://www.codementor.io/kratos/building-an-hello-world-application-with-python-django-95sysyr6v)

1. ***Launch django server*** 
  * Open the command console in windows and go to the virtual environment folder in my documents. (For doubts about this procedure validate the installation tutorial)
  * Start your virtual environment with the command:  `workon englishcourse`
  * Entry the command to create the first project:  `django-admin startproject myfirstproject`
    
    * Once you entry this command and execute it. In the folder called `virtualenvironments` will be created a folder with the name `myfirstproject`
    
    You should get something like ![myfirstproject](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/firstprojectcreation.png)

2. ***Create a first web application***
* Using the command console within the virtual environment get into the folder for the new django project created previously with the command:
 * `cd myfirstproject`

* Create the web application **hello** : `python manage.py startapp hello`

3. ***Configure the script called views.py for hello app***
* Let's leave the command console open and then let's move to the windows explorer files and open the file called **views.py** located in the folder hello of your django application.
  * Go to the path: `C:\Users\a_urrego\Documents\VirtualEnvironments\myfirstproject\hello`
  * Right click in the file **views.py**
  * Now copy and paste this code in the file:
  
  ```Python
  from __future__ import unicode_literals
  from django.shortcuts import render
  from django.views.generic import TemplateView

  class HomeView(TemplateView):
    template_name = 'index.html'
   ```
   Now your file should look like ![views file](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/viewsfiles.png)
   
4. ***Create template folder and index.html file for hello*** 
 * Go to the path: `C:\Users\a_urrego\Documents\VirtualEnvironments\myfirstproject\hello` 
 * Create a folder called `templates`
 * Go into the folder and create a file called `index.html`
 * Open the file and copy and paste this code:
 
 ```html
   <html>
   <head><title>Home Page</title></head>
   <body>
   Hello world, this is the first Owens page
   </body>
   </html>
 ```
 Now your file should look like ![index file](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/indexowen.png)
 
5. ***Configure the script called urls.py for myfirstproject*** 
 * Go to the path: `C:\Users\a_urrego\Documents\VirtualEnvironments\myfirstproject\myfirstproject` 
 * Right click on the file called **urls.py**
 * Now edit the file and replace the content with:
 
 ```Python
 from django.conf.urls import url
 from django.contrib import admin
 from hello.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]
 ```
 Now your file should look like ![urls file myproject](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/urlfilemyproject.png)
 
 6. ***Run the web server*** 
 * Go back into the console and logged in the  `virtual enviroment englishcourse`.
 * Go to the path `C:\Users\a_urrego\Documents\VirtualEnvironments\myfirstproject` and entry the command:
  * `python manage.py runserver`
 * Automatically the server will be running and you will get in the console:
   ![server running](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/runningmyfirstproject.png)
   
 7. ***Finally open the browser and see your first web application running***
 * Go to your chrome browser and type http://127.0.0.1:8000/
 * You should see your ![web](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/myfirstprojectweb.png) 

 
  
