"""A PostController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Post import Post


class PostController(Controller):
    """PostController Controller Class."""

    def __init__(self, request: Request):
        self.request = request


    def show(self, view: View):
        posts = Post.all()
        return view.render('posts', {'posts': posts})


    def single(self, view: View, request: Request):
        post = Post.find(request.param('id'))
        return view.render('single', {'post': post})


    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))
        return view.render('update', {'post': post})


    def store(self, request: Request):
        post = Post.find(request.param('id'))
        post.title = request.input('title')
        post.body = request.input('body')
        post.save()
        return 'post updated'

    def delete(self, request: Request):
        post = Post.find(request.param('id'))
        post.delete()
        return 'post deleted'