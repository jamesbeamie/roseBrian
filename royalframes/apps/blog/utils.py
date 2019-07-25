from rest_framework.exceptions import NotFound
from .models import Blog

class Utils:
    """
        Utilities class to check if the article and comment exists

    """

    def check_blog(self, id):
        # check if Comment exists
        try:
            blog = Blog.objects.get(pk=id)
            return blog
        except Blog.DoesNotExist:
            raise NotFound(
                {"error": "blog not found"})
