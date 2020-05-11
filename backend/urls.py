from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    ... other patterns here ...
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]
