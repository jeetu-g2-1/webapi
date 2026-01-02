import hashlib
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from api1.models import APIKey
from django.contrib.auth.models import User

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return None

        # Hash the incoming API key
        hashed_key = hashlib.sha256(api_key.encode()).hexdigest()

        try:
            # Try to find a matching active hashed key
            APIKey.objects.get(hashed_key=hashed_key, is_active=True)
        except APIKey.DoesNotExist:
            # Fetch the stored hashed key for Faceapi
            key_obj = APIKey.objects.get(name='Faceapi')
            stored_hashed_key = key_obj.hashed_key

            # Compare both
            if hashed_key == stored_hashed_key:
                debug_msg = "Hashed key matches Faceapi key but it is inactive"
            else:
                debug_msg = "Hashed key does not match Faceapi key"

            # Return JSON response with debug info
            raise AuthenticationFailed(detail={
                "message": "Invalid API Key",
                "debug": debug_msg,
                "sent_hashed_key": hashed_key,
                "stored_hashed_key": stored_hashed_key
            })
        user=User.objects.get(username='faceapi_service')

        return (user, None)
