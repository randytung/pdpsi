from brothers.models import PClass, Brother
from rest_framework import viewsets, status, generics
from serializers import BrotherSerializer, PClassSerializer
from rest_framework.views import APIView #class based views
from rest_framework.decorators import api_view #function based views
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request,format=None):
	return Response({
		'PClass' : reverse('class-list', request=request, format=format),
		'Brother_list' : reverse('brother-list', request=request, format=format)
		})


class ClassList(APIView):
	#retreiving data from backend
	def get(self, request, format=None):
		class_list = PClass.objects.all()
		serializer = PClassSerializer(class_list, many=True)
		return Response(serializer.data)


class BrotherList(APIView):
	def get(self, request, format=None):
		brothers = Brother.objects.all()
		serializer = BrotherSerializer(brothers, many=True)
		return Response(serializer.data)
