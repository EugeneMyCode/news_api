from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import TypeNews, News
from .serializers import TypeNewsSerializer, NewsSerializer, ListNewsSerializer
from django.shortcuts import get_object_or_404

# Возможные страницы
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_news': '/news',
        'Search news by typenews': 'news/?type_news=type_news_name',
        'exactly_news': '/news/pk',
        'Add_news': '/createnews',
        'Update_news': '/news/pk/update',
        'Delete_news': '/news/pk/delete',
        'all_typenews': '/typenews',
        'exactly_typenews': '/typenews/pk',
        'Add_typenews': '/createtypenews',
        'Update_typenews': '/typenews/pk/update',
        'Delete_typenews': '/typenews/pk/delete',
    }
  
    return Response(api_urls)

# Добавление новостей
@api_view(['POST'])
def add_news(request):
    news = NewsSerializer(data=request.data)
  
    if News.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if news.is_valid():
        news.save()
        return Response(news.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Вывод конкретной новости
@api_view(['GET'])
def exactly_news(request, pk):
    try:
        news = News.objects.get(id=pk)
    except News.DoesNotExist:
        news = None
    serializer = NewsSerializer(news, many=False)
    return Response(serializer.data)

# Вывод новостей (можно и с фильтрацией по типу новостей)
@api_view(['GET'])
def view_news(request):
    if request.query_params:
        news = News.objects.filter(**request.query_params.dict())
    else:
        news = News.objects.all()
  
    if news:
        serializer = ListNewsSerializer(news, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Обновление новости
@api_view(['POST'])
def update_news(request, pk):
    news = News.objects.get(pk=pk)
    data = NewsSerializer(instance=news, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Удаление новости
@api_view(['DELETE'])
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

# Добавить тип новости
@api_view(['POST'])
def add_typenews(request):
    typenews = TypeNewsSerializer(data=request.data)
  
    if TypeNews.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if typenews.is_valid():
        typenews.save()
        return Response(typenews.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Вывод конкретного типа новости
@api_view(['GET'])
def exactly_typenews(request, pk):
    try:
        typenews = TypeNews.objects.get(id=pk)
    except TypeNews.DoesNotExist:
        typenews = None
    serializer = TypeNewsSerializer(typenews, many=False)
    return Response(serializer.data)

# Вывод типов новостей
@api_view(['GET'])
def view_typenews(request):
    typenews = TypeNews.objects.all()
    serializer = TypeNewsSerializer(typenews, many=True)
  
    if typenews:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Обновление типа новости
@api_view(['POST'])
def update_typenews(request, pk):
    typenews = TypeNews.objects.get(pk=pk)
    data = TypeNewsSerializer(instance=typenews, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Удаление типа новости
@api_view(['DELETE'])
def delete_typenews(request, pk):
    typenews = get_object_or_404(TypeNews, pk=pk)
    typenews.delete()
    return Response(status=status.HTTP_202_ACCEPTED)