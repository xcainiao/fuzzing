import numpy as np
import random

args = [("", repr(t)) for t in ["a", "a"*0x100, "a"*0x1000, 0, 
         1, -1, 2**32, 2**32+1, 2**32-1, 2**64, 2**64+1, 
	2**64-1, [], (), {}, set(), (1,), ("a",)]]
callers = []
types = []

def register(func):
	global callers
	global args
	global types
        lines = func.split("\n") 
        caller = lines[-1]
        definer = "\n".join(lines[:-1]) + "\n"
        
        filtercall = "[obj for obj in dir(caller) if callable(getattr(caller, obj))]"
        execstring = definer + "\ncaller = " + caller
        execstring = execstring + "\n" + "out.append(caller)"
        execstring = execstring + "\n" + "out.append("+ filtercall +")\n"
        out = []
        try:
            exec(execstring, {"out":out, "np":np})
        except Exception as e:
            print e
            return
        ret = out[0]
        new_caller = out[1]

        if not ret.__class__ in types:
            types.append(ret.__class__)
            args.append((definer, caller))
            callers.append((definer, caller))
            for func in new_caller:
                callers.append((definer, caller+"."+func))
        elif not random.randint(0, 0x1000):
            args.append((definer, caller))
            callers.append((definer, caller))


def generate():
	funcid = random.randint(0, 2**64)
	funcstr = "def func_%x():\n    "% funcid

	defer, c = random.choice(callers)
	
	funcstr = funcstr + defer
	funcstr = funcstr + "return "
	funcstr = funcstr + c
	funcstr = funcstr + "("
	arglist = []
	for i in range(0, random.randint(0, 5)):
		defer, arg = random.choice(args)
	        funcstr = funcstr + defer 
		arglist.append(arg)

	funcstr = funcstr + ",".join(arglist)
	funcstr = funcstr + ")"
	funcstr = funcstr + "\n"
	funcstr = funcstr + "func_%x()"% funcid
	return funcstr	

def init():
	global callers
	global args
	global types
        exclude = [
                'lookfor', 'memmap', 'fromregex', 'fromfile', 
                'chararray','show_config', 'save', 'savez', 
                'savez_compressed','int_asbuffer']

	callers = [("", "np."+obj) for obj in dir(np) if obj not in exclude and callable(getattr(np, obj))]
	for defer, arg in args:
		types.append(eval(arg).__class__)












