""" Url router for the Text Area module
"""

from django.urls import re_path

from core_module_text_area_app.views.views import TextAreaModule

urlpatterns = [
    re_path(
        r"module-text-area", TextAreaModule.as_view(), name="core_module_text_area_view"
    ),
]
