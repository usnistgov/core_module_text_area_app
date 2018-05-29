core_module_text_area_app
=========================

Text Area module for the parser core project.

Quick start
===========

1. Add "core_module_text_area_app" to your INSTALLED_APPS setting
-----------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_module_text_area_app',
    ]

2. Include the core_module_text_area_app URLconf in your project urls.py
------------------------------------------------------------------------

.. code:: python

    url(r'^', include('core_module_text_area_app.urls')),