

## Based Class-Based View CRUD Project

I have created Simple CRUD Project in Django Using Django ModelForm. created the Based Class-Based View.
We can define the get(), post(), patch(), and delete() methods so that we can perform the CRUD operations.

Class-based views provide an alternative way to implement views as Python objects instead of functions. 
They do not replace function-based views.
  1. Base Class-Based Views / Base View
  2. Generic Class-Based Views / Generic View

Base class-based views can be thought of as parent views, which can be used by themselves or inherited from. They may not provide all the capabilities required for projects, in which case there are Mixins which extend what base views can do.
  1. View
  2. TemplateView
  3. RedirectView
   
   
![crud](https://user-images.githubusercontent.com/84769341/204024870-eed80e48-60c2-4ca3-b445-44655fededfb.png)


## Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04\
Django==3.4.1\



## Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject

```

2. Download this project template from GitHub

```bash
  git clone https://github.com/parshurampatil197/Base-Class-Base-View-CRUD-Project.git
  cd BaseCBV_CRUD_Project
  
```

3. Create a virtual environment and install django

```bash
  virtualenv venv --python=python3 ; 
  source venv/bin/activate; 

```

4. Install the dependencies needed to run the app:

```bash
  pip install -r requirements.txt

```


5. Run the project

```bash
  python manage.py runserver

```


