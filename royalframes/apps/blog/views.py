from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import BlogSerializer
from .models import Blog
from .utils import Utils

class CreateBlogAPiView(generics.ListCreateAPIView):
    """
        View class to create and fetch comments
    """
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = BlogSerializer

    kweryset = Blog.objects.all()
    util = Utils()

    def post(self, request, *args, **kwargs):
        '''This method creates a blog'''
        # slug = self.kwargs['slug']
        # article = self.util.check_article(slug)
        blog = request.data['blog']
        serializer = self.serializer_class(data=blog, context={
            'request': request
        })
        # author_profile = Profile.objects.get(user=request.user)
        # serializer.is_valid()
        serializer.save()
        result = {"message": "blog created"}
        result.update(serializer.data)
        return Response(result,
                        status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        '''This method gets all blogs'''
        # slug = self.kwargs['slug']
        # article = self.util.check_article(slug)
        blogs = self.kweryset
        serializer = self.serializer_class(blogs, context={'request':request}, many=True)
        return Response({"blogs": serializer.data
                         }, status=status.HTTP_200_OK)



                         


class BlogApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogSerializer
    util = Utils()
    kweryset = Blog.objects.all()

    def get(self, request, id, *args, **kwargs):
        '''This method gets a single blog by id'''

        # slug = self.kwargs['slug']
        # article = self.util.check_article(slug)
        # util = Utils()
        blog = self.util.check_blog(id)
        serializer = self.serializer_class(blog, context={
            'request': request
        })
        return Response({"blog": serializer.data})

    def delete(self, request, id, *args, **kwargs):
        '''This method deletes a blog'''

        # slug = self.kwargs['slug']
        blog = self.util.check_blog(id)
        # comment = self.util.check_comment(id)

        # Must implement authentication
        if request.user.pk == blog.author_profile.id:
            self.perform_destroy(blog)
            msg = "deleted_comment"
            return Response({
                "message": msg
            }, status=status.HTTP_200_OK)
        else:
            msg = "restricted"
            return Response({
                "message": msg
            }, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, id, *args, **kwargs):
        '''This method updates a comment'''

        # slug = self.kwargs['slug']
        # article = self.util.check_article(slug)
        blog = self.util.check_blog(id)
        if request.user.pk == blog.author_profile.id:
            existing_field = request.data.copy()
            blog.body = existing_field['blog']['body']

            serializer = BlogSerializer(
                instance=blog, data=existing_field['blog'], context={
                    'request': request
                })
            if serializer.is_valid():
                serializer.save(author_profile=blog.author_profile)
                msg = "update_success"
                return Response({
                    "message": msg
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            msg = {"error": "Unauthorized"}
            return Response({
                "message": msg
            }, status=status.HTTP_401_UNAUTHORIZED)