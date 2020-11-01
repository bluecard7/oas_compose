import yaml
import re

from compose.oas_objects.openapi import OpenAPI
from compose.prep_loader import PrepLoader
from compose.errormsg import fieldrequiredmsg

class OASSpecWriter:
    def __init__(self, fragment_dirname, root_fragname, specname):
        self.fragment_dirname = fragment_dirname
        self.root_fragname = root_fragname
        self.specname = specname
        self.prep_loader = PrepLoader()

    '''
    OpenAPI Spec (OAS) is defined here:
    https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md.
    '''
    def write_oas_spec(self):
        root = None
        with open(f'{self.fragment_dirname}/{self.root_fragname}', 'r') as root_fragment:
            root = yaml.safe_load(root_fragment)

        with open(self.specname, 'w') as spec: 
            self.spec = spec
            self.walk_oas_tree(OpenAPI, root)

        del self.spec
    
    def walk_oas_tree(self, objtype, objdict):
        for fieldname in objtype.field_order:
            fieldDesc = getattr(objtype, fieldname)
            required = fieldDesc.bare()

            name = self.field_satisfying_name(fieldname, objdict)
            if name is not None:
                data = self.take_data(objdict, name)
                yaml.dump({ fieldname: data }, self.spec)

            elif required:
                raise RuntimeError(fieldrequiredmsg(fieldname))

    def field_satisfying_name(self, fieldname, objdict):
        if fieldname in objdict:
            return fieldname

        elif f'pre{fieldname}' in objdict:
            return f'pre{fieldname}'

        return None

    def take_data(self, objdict, name):
        data = objdict[name]

        if re.match('^pre', name) is not None:
            prep = self.prep_loader.getprep(name)
            data = prep(self.fragment_dirname, data)
        
        del objdict[name]
        return data
