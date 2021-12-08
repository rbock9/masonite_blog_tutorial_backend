"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Blog Routes
    Get('/blog', 'BlogController@show'),
    Post('/blog/create', 'BlogController@store'),
    Get('/posts', 'PostController@show'),
    Get('/post/@id', 'PostController@single'),
    Get('/post/@id/update', 'PostController@update'),
    Post('/post/@id/update', 'PostController@store'),
    Get('/post/@id/delete', 'PostController@delete'),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
