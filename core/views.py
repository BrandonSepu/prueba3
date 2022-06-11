from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Alertas
from .serializer import AlertasSerializer

# Create your views here.

@api_view(['GET'])
def allAlertas(request):
    alerta = Alertas.objects.all()
    serializado = AlertasSerializer(alerta, many = True)
    return Response(serializado.data)

@api_view(['POST'])
def loadAlertas(request):
    serializado = AlertasSerializer(data=request.data)
    if serializado.is_valid():
        serializado.save()
    return Response(serializado.data)
