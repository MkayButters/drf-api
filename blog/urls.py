from .views import Post

urlpatterns = [
    path('', Post.as_view(), name = 'blog post')
    path('<int:pk/', blogRetrieveUpdateDestroy.as_view(), name = 'update')
]
