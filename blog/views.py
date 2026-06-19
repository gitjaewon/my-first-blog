from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer


def index(request):
    return render(request, 'blog/post_list.html')


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.publish()
        return Response(PostSerializer(post).data)