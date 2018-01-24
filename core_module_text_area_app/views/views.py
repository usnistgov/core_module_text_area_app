""" Text Area module
"""
from core_parser_app.tools.modules.views.builtin.textarea_module import AbstractTextAreaModule


class TextAreaModule(AbstractTextAreaModule):

    def _retrieve_data(self, request):
        """ Retrieve module's data

        Args:
            request:

        Returns:

        """
        data = ''
        if request.method == 'GET':
            if 'data' in request.GET:
                data = request.GET['data']
        elif request.method == 'POST':
            if 'data' in request.POST:
                data = request.POST['data']
        return data

    def _render_data(self, request):
        """ Return module's data rendering

        Args:
            request:

        Returns:

        """
        return ''
