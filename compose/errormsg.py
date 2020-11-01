def fieldrequiredmsg(fieldname):
    return f'could not find required field or its preprocessor: {fieldname}'

def nosuchprepmsg(prepname):
    return f'no preprocessor called {prepname} exists'