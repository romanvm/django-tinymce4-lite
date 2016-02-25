# coding: utf-8

import json
from traceback import print_exc
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.utils.html import strip_tags


def spell_check(request):
    """
    Returns a HttpResponse that implements the TinyMCE spellchecker protocol.
    """
    data = json.loads(request.body.decode('utf-8'))
    output = {'id': data['id']}
    error = None
    try:
        import enchant
        from enchant.checker import SpellChecker
        if data['params']['lang'] not in enchant.list_languages():
            raise RuntimeError
        checker = SpellChecker(data['params']['lang'])
        checker.set_text(strip_tags(data['params']['text']))
        output['result'] = {checker.word: checker.suggest() for err in checker}
    except ImportError:
        error = _('pyenchant package is not installed!')
        print_exc()
    except RuntimeError:
        error = _('Missing dictionary {0}!').format(data['params']['lang'])
        print_exc()
    except Exception:
        error = _('Unknown error!')
        print_exc()
    if error is not None:
        output['error'] = error
    return HttpResponse(json.dumps(output), content_type='application/json')


def filebrowser(request):
    try:
        fb_url = request.build_absolute_uri(reverse('fb_browse'))
    except:
        fb_url = request.build_absolute_uri(reverse('filebrowser:fb_browse'))
    return render(request, 'tinymce/filebrowser.js', {'fb_url': fb_url})
