def RegisterStructClass(variables):
    import sys
 
    if not isinstance(variables, str):
        print ('Members type {} need to be as {}.'.format(type(variables), type(str)))
		sys.exit(1)
 
    def __init__(self, *args):
        splitlines = variables.split()

        if len(splitlines) <> len(args):
            print ('Failed to read arguments.')
			sys.exit(1)
   
        [self.__dict__.setdefault(k, v) for (k, v) in zip(splitlines, args)]
 
    return type('__struct__', (object, ), {'__init__': __init__})