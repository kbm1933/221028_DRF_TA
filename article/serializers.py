from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    def get_author(self,obj):
        return obj.author.username
    class Meta:
        model = Article
        fields = '__all__'


