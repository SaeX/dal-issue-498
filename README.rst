Goal
====

This is to show what https://github.com/yourlabs/django-autocomplete-light/issues/498 is about.


Installation
============
* Django 1.10 (latest version)
* Python 2.7.12 32 bit (latest 2.x version)
* django-autocomplete-light 2.3.3 (latest 2.x version)
* django-crispy-forms (latest version)
* Go to the admin and add one or two `CodeText` objects

Note the latest version of bootstrap (both CSS and JS) is already included.


Reproducing
===========
When navigating to http://127.0.0.1:8000/app498/add/, clicking the 'Save' button doesn't do anything and yields `An invalid form control with name='code_text-autocomplete' is not focusable` in JS console when using Chrome 53 on Win10.

When doing a `pip install django==1.9.9`, everything seems to work fine. The issue only occurs wih Django 1.10.