from rest_framework.exceptions import NotFound
from .models import Blog

class Utils:
    """
        Utilities class to check if the article and comment exists

    """

    # def check_article(self, slug):
    #     # check if article exists
    #     try:
    #         article = Article.objects.get(slug=slug)
    #         return article
    #     except Article.DoesNotExist:
    #         raise NotFound(
    #             {"error": error_msg["no_slug"]})

    def check_blog(self, id):
        # check if Comment exists
        try:
            blog = Blog.objects.get(pk=id)
            return blog
        except Blog.DoesNotExist:
            raise NotFound(
                {"error": "blog not found"})
