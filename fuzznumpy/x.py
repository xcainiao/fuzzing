a = """def func_64d854907be017a():
    return np.RankWarning(("a",))
func_64d854907be017a()"""
line = a.split('\n')
print dir(line[-1])

print "\n".join(line[:-1])+"\n"
