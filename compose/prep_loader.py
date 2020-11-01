import re
from compose import preps
from compose.errormsg import nosuchprepmsg

class PrepLoader:
    def getprep(self, prepname):
        prefix_match = re.match('^pre', prepname)
        
        if prefix_match is None or not hasattr(preps, prepname):
            raise NotImplementedError(nosuchprepmsg(prepname))

        return getattr(preps, prepname)
