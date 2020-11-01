# oas-compose
oas-compose is what kustomize is for k8 config, but for OpenAPI specfication.
This tool is only meant for OAS v3.0.0+ and yaml.

## Why does this exist?
OpenAPI is a specification that defines APIs in a well defined format.
It also comes with a great suite of extensions. 
There's Swagger UI that allows you to visualize and play with the APIs on a browser,
and openapi-generator that can generate client and server code in many popular languages.

Unlike the conveniences that come with it, the spec file itself can be hard to manage.
As development happens, things change, including the API.
This means editing the response that a path returns, editing a request a path accepts, adding paths, deleting schema - the list goes on.
And these changes tend to cause merge conflicts in a file that easily spans 
100s of lines.
Not only that, but it becomes increasingly harder to navigate as the API grows.
To smooth these bumps out, oas-compose organizes the overall spec file into fragments, pieces of the specification that are contained in their own file.

## Features as of 10/29/20
- P(riority) 0:
    - store paths in separate files
    - store components in separate files
- P1
    - ???

## Usage
To run the script: 
```python
    python -m 
```
To run unit tests: python -m unittest discover -v -s test

Note: running this project as a script with -m to unify method of running 
both unittests and 
Also, since the tests hit the src code as well, imports don't work properly when running 

(...talk about how fragments look like, etc.)

## How to navigate this repository
Start from src/compose.py

## Possible extentions
- schemas of objects as python objects (futher utilizing pyyaml)
- define types and recursively walk through the tree to allow further simplicfications
in Info, components, etc.
(I tried using typing module to handle lists and dicts)
- BUT biggest pain points for me were the paths and components, which are at the top level of the OpenAPI object hiearchy, so I can't convince myself to go any further

## Future Tasks/Experiments:
- unit tests
- benchmarks converting text to yaml and back to text vs just doing text, del vs no del