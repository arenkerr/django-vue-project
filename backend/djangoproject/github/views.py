from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import GitHubAccount 

@api_view(['POST'])
@login_required
def link_github_account(request):
    code = request.data.get('code')
    if not code:
        return Response({'error': 'no code was provided'}, status=status.HTTP_400_BAD_REQUEST)

    token_url = "https://github.com/login/oauth/access_token"
    params = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code,
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(token_url, params=params, headers=headers)
    
    if response.status_code != 200:
        return Response({'error': 'Failed to get access token :('}, status=status.HTTP_400_BAD_REQUEST)

    access_token = response.json().get('access_token')

    # saves account to db
    github_account = GitHubAccount.objects.create(
        user=request.user,
        access_token=access_token,
    )
    
    return Response({'message': 'GitHub linked!', 'access_token': access_token})

@api_view(['GET'])
def github_callback(request):
    return Response({})

# @api_view(['GET'])
# def list_user_repositories(request):
    # get all public repos

    # create a webhook for each repo?
        # url = f"https://api.github.com/repos/{repo}/hooks"

    # return list of public repos

# @api_view(['POST'])
# def select_user_repository(request):
    # save selected repo to db

# @api_view(['POST'])
# def github_webhook(request):
    # parse webhook events here
