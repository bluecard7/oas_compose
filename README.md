# oas_compose
Usable only for OAS v3.0 in yaml forn.

## What's OpenAPI?
Here's an introduction straight from their [website](https://swagger.io/specification/):

> The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.

> An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.

## Why oas_compose?
OpenAPI is a great tool, but the spec file itself can be hard to manage.

As development happens, things change, including the API.
This means editing the response that a path returns, editing a request a path accepts, adding paths, deleting schema - the list goes on.
And these changes tend to cause frequent merge conflicts in a file that easily spans 
hundreds of lines. 
Not only that, but it becomes harder to navigate as the API grows.

With oas_compose, a developer can organize sections of the monolithic spec as smaller files/fragments. 
Then they can use the script to compose the full spec from the fragments.
More on this in the [Usage](#usage) section.

## Features
- store paths in separate files
- store components in separate files

## Usage
To run the script: 
```
python -m compose.entry -h
usage: entry.py [-h] [-d FRAGMENT_DIRNAME] [-r ROOT_FRAGNAME] [-o SPECNAME]

Compose OAS spec from fragments

optional arguments:
-h, --help           show this help message and exit
-d FRAGMENT_DIRNAME  directory containing OAS fragments
-r ROOT_FRAGNAME     name of fragment to start writing spec from, should be
                     in fragment_dir
-o SPECNAME          name of file to write spec to
```
To run unit tests:
```python
pytest
```


## Possible extentions
- schemas of objects as python objects (futher utilizing pyyaml)
- define types and recursively walk through the tree to allow further simplicfications
in Info, components, etc.
(I tried using typing module to handle lists and dicts)
- BUT biggest pain points for me were the paths and components, which are at the top level of the OpenAPI object hiearchy, so I can't convince myself to go any further
