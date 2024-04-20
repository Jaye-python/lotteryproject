from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from lotapp.models import Ticket
from lotapp.views import SalaryForLifeDraw
from .serializers import  TicketSerializer

class CreateTicketView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
class CreateDrawView(APIView):
    def post(self, request, *args, **kwargs):
        plays = request.data.get('plays', [])
        rtp = request.data.get('rtp', 0)
        prices = request.data.get('prices')        

        draw_result = SalaryForLifeDraw.draw(plays, rtp, prices, jackpot_amount=20000)
        return Response(draw_result)
