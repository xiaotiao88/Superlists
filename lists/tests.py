from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from django.template.loader import render_to_string

import re

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
         request=HttpRequest()
         response=home_page(request)
         expected_html=render_to_string('home.html')
#         self.assertEqual(response.content.decode(),expected_html)
#        self.assertTrue(response.content.startswith(b'<html>'))
#        self.assertIn(b'<title>To-Do lists</title>',response.content)
#        self.assertTrue(response.content.endswith(b'</html>'))
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         expected_html = re.sub(csrf_regex, '', expected_html)
         self.assertEqual(observed_html,expected_html)
    

    def test_home_page_can_save_a_POST_request(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)
        self.assertIn('A new list item',response.content.decode())
        expected_html=render_to_string(
            'home.html',
            {'new_item_text':'A new list item'}
            )
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        observed_html = re.sub(csrf_regex, '', response.content.decode())
        expected_html = re.sub(csrf_regex, '', expected_html)
        self.assertEqual(observed_html,expected_html)
#        self.assertEqual(response.content.decode(),expected_html)
        
