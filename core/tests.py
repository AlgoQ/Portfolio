from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from selenium import webdriver

from core.views import index

class HomePageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Kobe Janssens</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_atleast_one_job(self):
        self.browser.get('http://localhost:8000')

        jobsElement = self.browser.find_element('class name', 'jobs')

        jobsHtml = jobsElement.get_attribute('outerHTML')
        self.assertIn('job-section', jobsHtml)


    def test_atleast_one_project(self):
        self.browser.get('http://localhost:8000')

        projectsElement = self.browser.find_element('class name', 'projects')

        projectsHtml = projectsElement.get_attribute('outerHTML')
        self.assertIn('project-inner', projectsHtml)