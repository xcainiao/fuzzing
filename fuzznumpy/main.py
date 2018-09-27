import fuzz
import numpy as np
from ctypes import CDLL


test = CDLL("c/test.so")
test.init()
fuzz.init()

while 1:
	func = fuzz.generate()
        # func = """import numpy\nnumpy.half(-1).choose(numpy.void(1), numpy.broadcast_arrays((1,)))"""
        test.copybuff(func)
	try:
		exec(func, {"np":np})
	except Exception as e:
		# print e
                continue
        print func
        fuzz.register(func)
