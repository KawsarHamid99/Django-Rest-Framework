Json Web Token

Installation:
->pip install djangorestframework-simplejwt


1. for global authentication[for all view]:
	settings.py:
	REST_FRAMEWORK={
		"DEFAULT_AUTHENTICATION_CLASSES":(
			'rest_framework_simplejwt.authentication.JWTAuthentication',
		)}

or,

for local authentication:
	go to views.py 
	1. from rest_framework_simplejwt.authentication import JWTAuthentication <-- import authentication class
	2. after import JWTAuthentication use it inside authentication_classes
		authentication_classes=[JWTAuthentication]



2.Modify urls.py fo app:
	from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
	urlpatterns=[ 
 
    		path("",include(router.urls)),
    		path("gettoken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    		path('refreshtoken/',TokenRefreshView.as_view(),name="koken_refresh"),
   		path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
	]

** before use you have to install httpie: pip install httpie

********* how genearate token:
1. genarate token for access: 
	--->  http POST http://127.0.0.1:8000/gettoken/ username="kawsar" password="kawsar" 
	it will return access and return token.
	by default access token will be valid for 5 minute and refresh token will be valid one day.you can not get access to data without access token.

2. refresh token:
	-->http POST http://127.0.0.1:8000/refreshtoken/ refresh="<refresh token>"
	when access get invalid within in a day by using refresh token you can get another access token:
	  


3. to varify weather this token is valid or not:
	--> http POST http://127.0.0.1:8000/verifytoken/ token="< access token >"
	example:
	--> http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0NjYzNDM3LCJpYXQiOjE2ODQ2NjMxMzcsImp0aSI6IjBhMTE1ZjFmN2UwNzRkODNiMzhmN2YyMDhjZTYwNGQ2IiwidXNlcl9pZCI6MX0.6wyW4b7likJ2NAb8zY2L9fVwvjAzNFwLSfCi_0l1490"



********* how USE token:

1. to get data:
	http http://127.0.0.1:8000/studentapi/ "Authorization:Bearer <access token>"   <--studentapi is the path of viewsets urls, it can be changed.

2. to post data:

http -f POST http://127.0.0.1:8000/studentapi/ name='kabi' dept='eee' country='bd' "Authorization:Bearer <access token>" 

3. to update data:
http -f  PUT http://127.0.0.1:8000/studentapi/4/ name='kulfi' dept='EEE' country='uganda' "Authorization:Bearer <access token>"

4. to update data:
http -f PATCH http://127.0.0.1:8000/studentapi/4/ name='kulfi' dept='EEE' country='uganda' "Authorization:Bearer <access token>"

5. delete:
http -f DELETE http://127.0.0.1:8000/studentapi/4/ "Authorization:Bearer <access token>"


 


********** To modify default settings:
	settings.py 
	
	from datetime import timedelta
	SIMPLE_JWT={
    "ACCESS_TOKEN_LIFETIME":timedelta(minutes=10)
	}

for more read JWT documentation














