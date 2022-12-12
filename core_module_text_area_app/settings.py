""" Core module text area settings

Settings with the following syntax can be overwritten at the project level:
SETTING_NAME = getattr(settings, "SETTING_NAME", "Default Value")
"""
from django.conf import settings

if not settings.configured:
    settings.configure()

AUTO_ESCAPE_XML_ENTITIES = getattr(settings, "AUTO_ESCAPE_XML_ENTITIES", True)
""" bool: enable or not the auto escape of the XML predefined entities
"""

ENABLE_XML_ENTITIES_TOOLTIPS = getattr(
    settings, "ENABLE_XML_ENTITIES_TOOLTIPS", True
)
""" boolean: enable the xml entities warning tooltip on the GUI.
"""
