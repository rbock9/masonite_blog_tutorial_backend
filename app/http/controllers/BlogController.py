"""A BlogController Module."""

from app.Post import Post
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class BlogController(Controller):
    """BlogController Controller Class."""

    def __init__(self, request: Request):
        """BlogController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('blog')

    # New store Method
    def store(self, request: Request):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id
        )

        return 'post created'
