from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Widget
from .serializer import WidgetSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Widget-list/',
		'Detail View':'/Widget-detail/<str:pk>/',
		'Create':'/Widget-create/',
		'Update':'/Widget-update/<str:pk>/',
		'Delete':'/Widget-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def widgetList(request):
	widget = Widget.objects.all().order_by('-id')
	serializer = WidgetSerializer(widget, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def widgetCreate(request):
	serializer = WidgetSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def widgetDetail(request, pk):
	tasks = Widget.objects.get(id=pk)
	serializer = WidgetSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def widgetUpdate(request, pk):
	task = Widget.objects.get(id=pk)
	serializer = WidgetSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def widgetDelete(request, pk):
	task = Widget.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')