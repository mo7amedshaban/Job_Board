from rest_framework.response import Response

from .models import Job
from .serializer import JobSerializer

from rest_framework.decorators import api_view


@api_view(['GET'])
def joblistapi(request):
    job = Job.objects.all()
    data = JobSerializer(job, many=True).data
    return Response({'data': data})
