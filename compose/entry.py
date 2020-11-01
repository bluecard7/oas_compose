import argparse

from compose.oas_writer import OASSpecWriter

def compose(fragment_dirname, root_fragname, specname):
    writer = OASSpecWriter(fragment_dirname, root_fragname, specname)
    writer.write_oas_spec()

parser = argparse.ArgumentParser(description='Compose OAS spec from fragments')
parser.add_argument(
    '-d', dest='fragment_dirname', default='openapi', 
    help='directory containing OAS fragments'
)
parser.add_argument(
    '-r', dest='root_fragname', default='root.yaml', 
    help='name of fragment to start writing spec from, should be located in fragment_dir'
)
parser.add_argument(
    '-o', dest='specname', default='openapi.yaml', 
    help='name of file to write spec to'
)

args = parser.parse_args()
compose(args.fragment_dirname, args.root_fragname, args.specname)