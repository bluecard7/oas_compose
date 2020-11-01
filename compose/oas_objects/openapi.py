from .field import FieldDesc

class OpenAPI:
    openapi = FieldDesc(True)
    info = FieldDesc(True)
    servers = FieldDesc()
    paths = FieldDesc(True)
    components = FieldDesc()
    security = FieldDesc()
    tags = FieldDesc()
    externalDocs = FieldDesc()

    field_order = [
        'openapi', 'info', 
        'servers', 'paths', 
        'components', 'security', 
        'tags', 'externalDocs'
    ]    