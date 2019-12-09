from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/Contact/(?P<pk>[0-9]+)$',
        views.get_delete_update_contact,
        name='get_delete_update_contact'
    ),
    url(
        r'^api/v1/Contact/$',
        views.get_post_contact,
        name='get_post_contact'
    ),
    url(r'^api/v1/home',
        views.get_delete_update_home,
        name='get_post_home'),
    url(r'^api/v1/user',
        views.get_post_user,
        name='get_post_user'),
    url(r'^api/v1/database',
        views.get_database, name='get_post_database'),
    url(r'^api/v1/login',
        views.user_login,
        name='get_login'),
    url(r'^api/v1/About',
        views.get_about,
        name='get_login')

]