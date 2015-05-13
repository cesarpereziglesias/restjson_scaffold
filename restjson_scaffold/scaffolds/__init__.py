from pyramid.scaffolds import PyramidTemplate

class RestJsonTemplate(PyramidTemplate):

    _template_dir = 'restjson_scaffold'
    summary = 'Template to do REST/JSON services'

    def pre(self, command, output_dir, vars):
        vars["project_cc"] = self._to_camel_case(vars["project"])
        return PyramidTemplate.pre(self, command, output_dir, vars)

    def _to_camel_case(self, name):
        pieces = name.split('-')
        return ''.join([piece.capitalize() for piece in pieces])
