# coding: utf-8

import json
from selenium.webdriver import PhantomJS
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
try:
    from unittest import mock
except ImportError:
    import mock


class RenderTinyMCEWidgetTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = PhantomJS()
        super(RenderTinyMCEWidgetTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(RenderTinyMCEWidgetTestCase, self).tearDown()

    def test_rendering_tinymce4_widget(self):
        # Test if TinyMCE 4 widget is actually rendered by JavaScript
        self.browser.get(self.live_server_url + reverse('create'))
        self.browser.find_element_by_id('mceu_16')

    def test_rendering_with_different_language(self):
        with self.settings(LANGUAGE_CODE='fr-fr'):
            self.browser.get(self.live_server_url + reverse('create'))
            self.browser.find_element_by_id('mceu_16')
            self.assertTrue('Appuyer sur ALT-F9 pour le menu.' in
                            self.browser.page_source)

    def test_rendering_tinymce4_admin_widget(self):
        # Since emulating login with Selenium is too much fuss
        # we test only basic functionality
        User.objects.create_superuser('test', 'test@test.com', 'test')
        self.client.login(username ='test', password='test')
        response = self.client.get('/admin/test_tinymce/testmodel/add/', follow=True)
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
