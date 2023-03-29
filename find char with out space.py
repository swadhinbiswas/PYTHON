def inf_gen(began =0):
   while True:
         yield began
         began += 1
g= inf_gen(100)

print(next(g))