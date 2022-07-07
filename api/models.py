from django.db import models

# Модель для типов новостей
class TypeNews(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'typenews'

    def __str__(self) -> str:
        return self.name
 
# Модель для новостей
class News(models.Model):
    type_news = models.ForeignKey(TypeNews, to_field='name', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    small_description = models.CharField(max_length=100)
    full_description = models.TextField()

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self) -> str:
        return self.name