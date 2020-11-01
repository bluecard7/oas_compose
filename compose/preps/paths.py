import yaml

def prepaths(fragment_dirname, path_fragnames):
    paths = dict()
    for fragname in path_fragnames:
        with open(f'{fragment_dirname}/{fragname}') as path_fragment:
            path_yaml = yaml.safe_load(path_fragment)
            for path, operations in path_yaml.items():
                paths[path] = operations
                
    return paths