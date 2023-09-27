from django_filters import FilterSet # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Category
 
 
# создаём фильтр
class PostFilter(FilterSet):
   class Meta:
        model = Post
        fields = {
            'title': ['icontains'], 
            # мы хотим чтобы нам выводило название статьи хотя бы отдалённо похожее на то, что запросил пользователь
            'dateCreation': ['gt'], 
            # дата публикации должна быть больше или равно тому, что указал пользователь
            'text': ['icontains'], 
            'author': ['exact'], # фильтр по автору, что выбрал пользователь
        }
        # = ('dateCreation', 'author') # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)