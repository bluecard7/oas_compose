from collections import defaultdict
import yaml

def precomponents(fragment_dirname, component_fragnames):
    components = defaultdict(dict)
    for fragname in component_fragnames:
        with open(f'{fragment_dirname}/{fragname}') as fragment:
            components_yaml = yaml.safe_load(fragment)
            for component_type, models in components_yaml.items():
                merge_modeldicts(components[component_type], models)
                
    return components

def merge_modeldicts(modeldst, modelsrc):
    for modelname, model in modelsrc.items():
        modeldst[modelname] = model