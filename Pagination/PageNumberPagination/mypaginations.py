from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination,CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=2
    page_query_param='p'
    
    page_size_query_param='records'
    #clint will choose page size http://127.0.0.1:8000/perview/perviewpagination/?p=2&records=3
    

    max_page_size=7
    #maximum page size will be 7[records=7] even if clinte choose more then 7 like 7,8,10. it will autometiclally be 7.

    last_page_strings='end'

class MyLimitOffsetPagination(LimitOffsetPagination):

    # pass #it will use default settings.
    #http://127.0.0.1:8000/limit_shaffle/?limit=2&offset=2
    
    # modification
    default_limit=5
    limit_query_param ='mylist'
    offset_query_param='myoffset'
    max_limit=6


class MyCursorPagination(CursorPagination):
    page_size=3
    ordering='name'
    cursor_query_param="cursor"
