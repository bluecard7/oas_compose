import yaml

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
    
    def walk_oas_tree(self, obj_type, obj_dict):
        for fieldname in obj_type.field_order:
            fieldDesc = getattr(obj_type, fieldname)
            required = fieldDesc.bare()
            prepname = f'pre{fieldname}'

            if fieldname in obj_dict:
                data = obj_dict[fieldname]
                self.write_to_spec({ fieldname: data })
                del obj_dict[fieldname]

            elif prepname in obj_dict:
                prep = self.prep_loader.getprep(prepname)
                data = obj_dict[prepname]
                prepped_data = prep(self.fragment_dirname, data)
                self.write_to_spec({ fieldname: prepped_data })
                del obj_dict[prepname]

            elif required:
                raise RuntimeError(fieldrequiredmsg(fieldname))

    def write_to_spec(self, field):
        yaml.dump(field, self.spec)