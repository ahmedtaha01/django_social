from account.models import Auser
from django.http import HttpResponse ,request , Http404
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from urllib.error import HTTPError



# def save_profile(backend, user, response, *args, **kwargs):
#     pass
#     # return HttpResponse(response.get('picture'))
#     # user = Auser()
#     # # #return HttpResponse(make_password(response.get('name')))
#     # # user.username = response.get('name')
#     # user.email = response.get('email')
#     # #return HttpResponse(response.get('email'))
#     # # user.password = make_password(response.get('id'))
#     # user.save()


# def save_profile(backend, user, response, is_new=False, *args, **kwargs):
#     if is_new and backend.name == "facebook":
#         # The main part is how to get the profile picture URL and then do what you need to do
#         Auser.objects.filter(owner=user).update(
#             imageUrl='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
#                                                                                                   response[
#                                                                                                       'access_token']))
#     elif backend.name == 'google-oauth2':
#         if is_new and response.get('picture'):
#             Auser.objects.filter(owner=user).update(imageUrl=response['picture'])


# def save_profile(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     if backend.name == 'facebook':
#         url = "https://graph.facebook.com/%s/picture?type=large"%response['id']
#     if backend.name == 'twitter':
#         url = response.get('profile_image_url', '').replace('_normal','')
#     if backend.name == 'google-oauth2':
#         url = response['image'].get('url')
#         ext = url.split('.')[-1]
#     if url:
#         user.picture = url
#         user.save()


def save_profile(backend, strategy, details, response,
        user=None,is_new=False, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        # url = "https://graph.facebook.com/%s/picture?type=large"%response['id']
        # url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        url='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
                                                                                              response[
                                                                                                  'access_token'])
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]
    if url:
        if is_new:    #already registered
            user.get_image_from_url(url)
            user.save()
