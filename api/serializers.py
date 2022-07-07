from django.db.models import fields
from rest_framework import serializers
from .models import TypeNews, News

# Сериализатор для типов новостей
class TypeNewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypeNews
    fields = ('name', 'color')

# Сериализатор для новостей
class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = ('name', 'small_description', 'full_description', 'type_news')

# Сериализатор только для страницы вывода всех новостей
class ListNewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = ('name', 'small_description', 'type_news')