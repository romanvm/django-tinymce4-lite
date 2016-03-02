# coding: utf-8

import json
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
try:
    from unittest import mock
except ImportError:
    import mock


class RenderTinyMCEWidgetTestCase(TestCase):
    def test_rendering_tinymce4_widget(self):
        response = self.client.get(reverse('create'))
        self.assertContains(response, 'tinymce.min.js')
        self.assertContains(response, 'tinyMCE.init(')

    def test_rendering_tinymce4_admin_widget(self):
        User.objects.create_superuser('test', 'test@test.com', 'test')
        client = Client()
        client.login(username ='test', password='test')
        response = client.get('/admin/test_tinymce/testmodel/add/', follow=True)
        self.assertContains(response, 'tinymce.min.js')
        self.assertContains(response, 'tinyMCE.init(')


class SpellCheckViewTestCase(TestCase):
    def test_spell_check(self):
        import enchant
        languages = enchant.list_languages()
        lang = 'en_US'
        if lang not in languages:
            lang = lang[:2]
            if lang not in languages:
                raise RuntimeError('Enchant package does not have English spellckecker dictionary!')
        text = 'The quick brown fox jumps over the lazy dog.'
        data = {'id': '0', 'params': {'lang': lang, 'text': text}}
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertTrue('result' in json.loads(response.content.decode('utf-8')))
        text = 'The quik brown fox jumps ower the lazy dog.'
        data['params']['text'] = text
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        result = json.loads(response.content.decode('utf-8'))['result']
        self.assertEqual(len(result), 2)

    def test_missing_dictionary(self):
        data = {'id': '0', 'params': {'lang': 'fo_BA', 'text': 'text'}}
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertTrue('error' in json.loads(response.content.decode('utf-8')))


class CssViewTestCase(TestCase):
    def test_css_view(self):
        response = self.client.get(reverse('tinymce-css'))
        self.assertContains(response, 'margin-left')


class FileBrowserViewTestCase(TestCase):
    @mock.patch('tinymce.views.reverse')
    def test_filebrowser_view(self, mock_reverse):
        mock_reverse.return_value = '/filebrowser'
        response = self.client.get(reverse('tinymce-filebrowser'))
        self.assertContains(response, '/filebrowser')
