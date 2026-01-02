import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api1.authentication import APIKeyAuthentication
from api1.logic import compute_face_distance
from api1.models import FaceImageResponse,APIRequestLog

 
class FaceVerificationAPI(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]
 
    def post(self, request):
        APIRequestLog.objects.create(
    ip_address=request.META.get("REMOTE_ADDR"),
    method=request.method,
    path=request.path,
    content_type=request.content_type,
    content_length=request.META.get("CONTENT_LENGTH"),
    headers=dict(request.headers),
    body=request.body.decode(errors="ignore")[:10000],  # limit size
    parsed_data=request.data if isinstance(request.data, dict) else {},
    files_count=len(request.FILES),
    user_agent=request.META.get("HTTP_USER_AGENT"),
)


        

        # 1. Check Content-Type
        if request.content_type != "application/json":
            return Response({"error": "Content-Type must be application/json"}, status=111)

        # 2. Check body is JSON
        if not isinstance(request.data, dict):
            return Response( {"error": "Invalid JSON body"},status=222)
        


        
        # 3. Check required fields
        # required_fields = ["original_img_response", "face_img_response"]
        # missing = [f for f in required_fields if not request.data.get(f)]
        # if missing:
        #     return Response({"error": "Invalid request format","missing_fields": missing},status=333)
        # else:
        #     original_img = request.data.get("original_img_response")
        #     face_img = request.data.get("face_img_response")

        similarity=0.5         #round(face_result,1)
        if similarity <= 0.8:
            return Response(
        {
            "statusCode":200,
            "body":{
                "distance": similarity
            },
            "message":"Success",
        }
    )
        else:
            return Response(
        {
            "message":"Forbidden",
        }
    )
















# If we reach here → format is correct




# if not original_img and not face_img:
#     return Response(
#         {"error": "Both images are required"},
#         status=300
#     )
# elif not face_img:
#     return Response(
#         {"error":"Face image is requried"},
#         status=305
#     )
# elif not original_img:
#     return Response({"error":"Original image is required"},
#                     status=310)


# FaceImageResponse.objects.create(
# original_img_response=original_img,
# face_img_response=face_img)

# #face_result=compute_face_distance(original_img,face_img)


        
 
    
    
    