

class Parameter(object):
    def __setattr__(self, attr, value):
        # print("set %s to %s" % (attr, value))
        super().__setattr__(attr, value)