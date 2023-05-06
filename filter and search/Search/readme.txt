------------------*****---------------
1. import SearchFilter form rest_framework.filters in "views.py"
2. use SearchFilter in filter_backends and insert the search column name in search_field [shown in views.py]


------------------*****---------------
    i.   search_field=[^name]   <-------- start with search_field
    ii.  search_field=[=name]   <-------- Exact match
    iii. search_field=[@name]   <-------- full-text search(currently only support in django postgresql) 



------------------*****---------------
 "http://127.0.0.1:8000/studentview/?search=k"   hear you can see that "search=k"
  
  if you use other word in place of search, ->
        add this code in "settings.py"
            REST_FRAMEWORK={
                'SEARCH_PARAM':'q'
            }

 "http://127.0.0.1:8000/studentview/?q=k" here you will use "q=kawsar" in place of "search=kawsar"




------------------*****---------------
Ordering Filter

1. at first import the OrderingFilter form rest_framework.filters [views.py]
2. thn use it in filter_backends=[OrderingFilter] at views.py
3. thn use ordering_fields=['name'] or ordering_fields=['name','city'] or ordering_filters="__all__"
