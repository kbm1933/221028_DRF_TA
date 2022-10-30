from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     serializer = ArticleSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save(author=request.data)
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        article = ArticleSerializer(data=request.data)
        article.is_valid(raise_exception=True)
        article.save(author=request.user)
        return Response(article.data)
