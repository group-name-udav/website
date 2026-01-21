from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer

def item_list(request):
    items = MediaItem.objects.all()
    return render(request, 'reviews/item_list.html', {'items': items})

@api_view(['GET', 'POST'])
def item_api_list(request):
    # GET: Retrieve data in JSON format
    if request.method == 'GET':
        items = MediaItem.objects.all()
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

    # POST: Create new data via API
    elif request.method == 'POST':
        serializer = MediaItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def item_detail(request, pk):
    item = MediaItem.objects.get(pk=pk)
    # Get reviews specifically for this item
    reviews = item.reviews.all() 
    return render(request, 'reviews/item_detail.html', {'item': item, 'reviews': reviews})