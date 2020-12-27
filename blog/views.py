from rest_framework.generics import ListCreateAPIView, RetriveUpdateDestroyAPIView,
from .models import blog

class Post(ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blog

class BlogRetrieveUpdateDestroyAPIView(RetriveUpdateDestroyAPIView):
    queryset = blog.objects.all()
    serializer_class = blog
    permission_classes = (IsPurchaserOrReadOnly,)
