class Interval:

    type_name = {0:'tick',
                 1:'m1',
                 2:'m5'}
    
    name_type = {v:k for k,v in type_name.items()}
    names = list(name_type.keys())

    def __init__(self, value='m1'):
        if value not in self.names:
            return AssertionError, 'Interval value not exists'
        self.type = self.name_type[value]

    def get_name(self):
        return self.type_name[self.type]
    
    def get_type(self):
        return self.type
