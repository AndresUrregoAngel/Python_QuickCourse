### Installing Django

#### Prepare a virtual environment / Install server

1. ***Verify the current python version.***

  * Python --version
  
    ![Python version](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/pythonversion.png)
  
2. ***Execute:*** [Documentation Virtualenv](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#lsvirtualenv)

  * pip install virtualenv
  * pip install virtualenvwrapper-win

3. ***Create a virtual environment:*** 

  * Create a folder called `VirtualEnvironments` in my documents (mis documentos).
  
  * Create the virtual environment englishcourse. 
  
    1. [How to open or access in the windows console command](https://www.digitalcitizen.life/7-ways-launch-command-prompt-windows-7-windows-8)
    2. `cd C:\Users\a_urrego\Documents\VirtualEnvironments` replace the folder path with your own.       
    3. Type python to go in console mode for python.    
    4. Entry the code: [source](https://stackoverflow.com/questions/647515/how-can-i-get-python-path-under-windows)      
      `import os`      
      `import sys`       
      `print(os.path.dirname(sys.executable))`
      
      *Example:*      
      ![Python Executable](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/pythonexecutable.png)
      
    5. Take the note of the python path.
    6. type `exit()` to close the python execution. Then you will keep going in the command console under the folder `VirtualEnvironments`.
    7. Now we are ready to create the virtual environment so type the code:
      * `mkvirtualenv --python=<python execution path\python.exe> englishcourse`
      * Andres case: `mkvirtualenv --python=C:\Users\a_urrego\AppData\Local\Programs\Python\Python36-32\python.exe englishcourse`

    So, python will create the required environment and preinstall an isolated python version completely independent of your windows environment. At the end of this operation you should be already logged in this virtual environment watching the name and the begining of the command line as the example below:
  
   ![Logged in VM](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/loggedvm.png)
   
   8. Install django with the command: `pip install django`
   
   ![Django Installation](https://github.com/AndresUrregoAngel/librarydocs/tree/master/python_course/images/djangoinistalled.png)
   
   9. Finally run a command to validate the django version installed: `django-admin  --version`
   10. To exist from the virtual environment type `deactivate`
   11. To loging again in the environment use `workon englishcourse`
   
   
  
      
    
    
      
  
    

  



  
  
