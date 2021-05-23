from decorators.models import Entry
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
import time

def user_is_entry_author(func):
    def wrapper(request, *args, **kwargs):
        entr_obj = Entry.objects.get(id=kwargs['id'])
        if entr_obj.created_by == request.user:
            return func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper

def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return _inner

def timeit(method):

   def timed(*args, **kw):
       ts = time.time()
       result = method(*args, **kw)
       te = time.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result

   return timed
