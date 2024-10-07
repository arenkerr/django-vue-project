import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth import login

class GoogleLogin(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "token required"}, status=status.HTTP_400_BAD_REQUEST)

        google_response = requests.get(
            'https://oauth2.googleapis.com/tokeninfo',
            params={'id_token': token}
        )

        if google_response.status_code != 200:
            return Response({"error": "bad token"}, status=status.HTTP_400_BAD_REQUEST)

        google_data = google_response.json()
        email = google_data.get('email')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(
                email=email,
                first_name=google_data.get('given_name'),
                last_name=google_data.get('family_name'),
            )

        login(request, user)
        return Response({"message": "Logged in!!!"}, status=status.HTTP_200_OK)
