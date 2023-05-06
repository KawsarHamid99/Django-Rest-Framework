------------------*****---------------
page number pagination
    1.  Globally for all pages: just add this code in settings.py
        
        REST_FRAMEWORK={
        'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE':3
        }
    
------------------*****---------------
per view pagination
    2. per view pagination:you can use pagination in every class and you can custom your pagination for each class
        i.  first make mypagination.py and work on it[detail has been shown in mypagination.py] 
        ii. import the class in views.py[shown in views.py at perViewPagination class ]


------------------*****---------------
LimitOffsetPagination
    3. 

    
------------------*****---------------
CursorPaginition
    4. 