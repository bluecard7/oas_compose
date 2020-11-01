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
python -m compose.entry
usage: entry.py [-h] [-d FRAGMENT_DIRNAME] [-r ROOT_FRAGNAME] [-o SPECNAME]

Compose OAS spec from fragments

optional arguments:
-h, --help           show this help message and exit
-d FRAGMENT_DIRNAME  directory containing OAS fragments (default: openapi)
-r ROOT_FRAGNAME     name of fragment to start writing spec from, should be
                     in fragment_dir (default: root.yaml)
-o SPECNAME          name of file to write spec to (default: openapi.yaml)
```
To run unit tests:
```python
pytest
``` 

### Examples of fragments:

root.yaml
```yaml
openapi: 3.0.0

info:
  title: Sample API
  description: Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.
  version: 0.1.9

servers:
  - url: http://api.example.com/v1
    description: Optional server description, e.g. Main (production) server
  - url: http://staging-api.example.com
    description: Optional server description, e.g. Internal staging server for testing

# The fields below are preprocessor labels. 
# They are identified by the 'pre' prefixing the field name that it stands in for
# There are corresponding functions named the same as the labels in the preps module,
# the actual preprocesseors that prep the files
prepaths:
  - some_path_fragment1.yaml
  - some_path_fragment2.yaml

precomponents:
  - some_component_fragment1.yaml
  - some_component_fragment2.yaml
  - some_component_fragment3.yaml
``` 

some_path_fragment.yaml
```yaml
/admin:
  get:
    summary: Returns a list of users.
    description: Optional extended description in CommonMark or HTML.
    responses:
    '200':    # status code
      description: A JSON array of user names
      content:
        application/json:
          schema: 
            type: array
          items: 
            type: string
```

some_component_fragment.yaml
```yaml
parameters:
  offsetParam:
    name: offset
    in: query
    description: Number of items to skip before returning the results.
    required: false
    schema:
      type: integer
      format: int32
      minimum: 0
      default: 0

  limitParam:
    name: limit
    in: query
    description: Maximum number of items to return.
    required: false
    schema:
      type: integer
      format: int32
      minimum: 1
      maximum: 100
      default: 20
```