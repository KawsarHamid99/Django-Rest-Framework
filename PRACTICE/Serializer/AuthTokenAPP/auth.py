from rest_framework.authtoken.views import ObtainAuthToken,obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthtoken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,"user_id":user.pk,"email":user.email})

