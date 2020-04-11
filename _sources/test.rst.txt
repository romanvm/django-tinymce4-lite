Test Project
============

The **tinymce4-lite** sources include **test_tinymce** project that can be used to run automated tests
or to try a live TinyMCE 4 editor widget. The test project can also serve as a basic example of
**tinymce4-lite** usage.

To use the test project, first you need to install the necessary dependencies::

  $ pip install -r requirements.txt

Then you need to create the test database::

  $ python manage.py migrate

If you want to try TinyMCE in Django Admin, create a superuser to access the Admin interface::

  $ python manage.py createsuperuser

To run automated tests, enter in the console::

  $ python manage.py test test_tinymce

Tests require web-browsers: Firefox on Windows and Chrome on other platforms.
You also need to download respective Selenium drivers for your platform:
`Gecko driver <https://github.com/mozilla/geckodriver/releases>`_ or
`Chrome driver <https://sites.google.com/a/chromium.org/chromedriver/>`_.
Set the necessary permissions for a driver executable and add the directory
where it resides your system ``PATH`` environment variable.
Also check Travis CI configuration ``.travis.yml``.

To open TinyMCE 4 editor, run the test server::

  $ python manage.py runserver

Then open the project's start page in your browser: http://127.0.0.1:8000.
The browser will open a webpage with a TinyMCE 4 editor.

.. note:: The commands described in this section need to be run from the **tinymce4-lite**
  sources root directory.

The test project is very simple. It allows you to try rich text editing in
TinyMCE 4 and then save the text and see how it looks on a web-page.
