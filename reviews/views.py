from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem, Review
from .serializers import MediaItemSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import ReviewForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Save users to db.sqlite3
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') # After registrtion redirect to login
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})

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

@api_view(['GET', 'PUT', 'DELETE'])
def item_api_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)

    if request.method == 'GET':
        serializer = MediaItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MediaItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def item_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    reviews = item.reviews.all()
    
    user_review_exists = False
    if request.user.is_authenticated:
        user_review_exists = Review.objects.filter(item=item, author=request.user).exists()

    if request.method == 'POST' and not user_review_exists:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.author = request.user
            review.save()
            return redirect('item_detail', pk=pk)
    else:
        form = ReviewForm(initial={'item': item})

    return render(request, 'reviews/item_detail.html', {
        'item': item, 
        'reviews': reviews, 
        'form': form,
        'user_review_exists': user_review_exists
    })

def search(request):
    query = request.GET.get('q')
    if query:
        results = MediaItem.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'reviews/search.html', {'results': results, 'query': query})