# coding: utf-8
# License: MIT, see LICENSE.txt
"""
django-tinymce4-lite views
"""

from __future__ import absolute_import
import json
import logging
from django import VERSION
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.views.decorators.cache import never_cache
from jsmin import jsmin
try:
    from enchant import checker, list_languages
except ImportError:
    pass

__all__ = ['spell_check', 'spell_check_callback', 'css', 'filebrowser']

logging.basicConfig(format='[%(asctime)s] %(module)s: %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def spell_check(request):
    """
    Implements the TinyMCE 4 spellchecker protocol

    :param request: Django http request with JSON-RPC payload from TinyMCE 4
        containing a language code and a text to check for errors.
    :type request: django.http.request.HttpRequest
    :return: Django http response containing JSON-RPC payload
        with spellcheck results for TinyMCE 4
    :rtype: django.http.JsonResponse
    """
    data = json.loads(request.body.decode('utf-8'))
    output = {'id': data['id']}
    error = None
    status = 200
    try:
        if data['params']['lang'] not in list_languages():
            error = 'Missing {0} dictionary!'.format(data['params']['lang'])
            raise LookupError(error)
        spell_checker = checker.SpellChecker(data['params']['lang'])
        spell_checker.set_text(strip_tags(data['params']['text']))
        output['result'] = {spell_checker.word: spell_checker.suggest()
                            for err in spell_checker}
    except NameError:
        error = 'The pyenchant package is not installed!'
        logger.exception(error)
    except LookupError:
        logger.exception(error)
    except Exception:
        error = 'Unknown error!'
        logger.exception(error)
    if error is not None:
        output['error'] = error
        status = 500
    return JsonResponse(output, status=status)


@never_cache
def spell_check_callback(request):
    """
    JavaScript callback for TinyMCE4 spellchecker function

    :param request: Django http request
    :type request: django.http.request.HttpRequest
    :return: Django http response with spellchecker callback JavaScript code
    :rtype: django.http.HttpResponse
    """
    return HttpResponse(
        jsmin(render_to_string('tinymce/spellcheck-callback.js',
                               request=request)),
        content_type='application/javascript; charset=utf-8')


@never_cache
def css(request):
    """
    Custom CSS for TinyMCE 4 widget

    By default it fixes widget's position in Django Admin

    :param request: Django http request
    :type request: django.http.request.HttpRequest
    :return: Django http response with CSS file for TinyMCE 4
    :rtype: django.http.HttpResponse
    """
    if 'grappelli' in settings.INSTALLED_APPS:
        margin_left = 0
    elif VERSION[:2] <= (1, 8):
        margin_left = 110  # For old style admin
    else:
        margin_left = 170  # For Django >= 1.9 style admin
    # For Django >= 2.0 responsive admin
    responsive_admin = VERSION[:2] >= (2, 0)
    return HttpResponse(render_to_string('tinymce/tinymce4.css',
                                         context={
                                             'margin_left': margin_left,
                                             'responsive_admin': responsive_admin
                                         },
                                         request=request),
                        content_type='text/css; charset=utf-8')


@never_cache
def filebrowser(request):
    """
    JavaScript callback function for `django-filebrowser`_

    :param request: Django http request
    :type request: django.http.request.HttpRequest
    :return: Django http response with filebrowser JavaScript code for for TinyMCE 4
    :rtype: django.http.HttpResponse

    .. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
    """
    try:
        fb_url = reverse('fb_browse')
    except:
        fb_url = reverse('filebrowser:fb_browse')
    return HttpResponse(jsmin(render_to_string('tinymce/filebrowser.js',
                                               context={'fb_url': fb_url},
                                               request=request)),
                        content_type='application/javascript; charset=utf-8')
