from compose import preps
from compose.errormsg import nosuchprepmsg

class PrepLoader:
    def getprep(self, prepname):
        if not hasattr(preps, prepname):
            raise NotImplementedError(nosuchprepmsg(prepname))

        return getattr(preps, prepname) 
