import argparse
from compose.oas_writer import OASSpecWriter

def compose(fragment_dirname, root_fragname, specname):
    writer = OASSpecWriter(fragment_dirname, root_fragname, specname)
    writer.write_oas_spec()

parser = argparse.ArgumentParser(description='Compose OAS spec from fragments')
parser_arguments = [
    ['-d', 'fragment_dirname', 'openapi', 'directory containing OAS fragments'],
    ['-r', 'root_fragname', 'root.yaml', 'name of fragment to start writing spec from, should be in fragment_dir'],
    ['-o', 'specname', 'openapi.yaml', 'name of file to write spec to'],
]

for option, dest_name, default_value, help_msg in parser_arguments:
    parser.add_argument(option, dest=dest_name, default=default_value, help=help_msg)

args = parser.parse_args()
compose(args.fragment_dirname, args.root_fragname, args.specname)
