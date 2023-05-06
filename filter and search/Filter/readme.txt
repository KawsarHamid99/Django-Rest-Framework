1. normal filtering: just use get_queryset function in views.py file, inside the class.[showes in views.py of filterapp]

2. use gnerice filtering : 
    i. install djanfo-filter: pip install django-filter
    ii. add 'django_filters' in django's installed_apps in settings.py 
    iii. add DjangoFilterBackend at settings.py [added under STATIC_URL]
    iv. use DjangoFilterBackend in views.py at GenericFilterApp.