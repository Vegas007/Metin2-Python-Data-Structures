def RegisterStructClass(members):
	import sys
 
    if not isinstance(members, str):
		print ('Members type {} need to be as {}.'.format(type(members), type(str)))
		sys.exit(1)
 
	def __init__(self, *args):
		split_lines = members.split()

		if len(split_lines) <> len(args):
			print ('Failed to read arguments.')
			sys.exit(1)
   
		[self.__dict__.setdefault(k, v) for (k, v) in zip(split_lines, args)]
 
	return type('__struct__', (object, ), {'__init__': __init__})
