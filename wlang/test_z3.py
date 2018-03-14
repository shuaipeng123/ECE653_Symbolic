import z3
import pdb
a=2
b=3
#pdb.set_trace()
c=a+b
kids=[1,2,3]
for kid in kids:
    kid=kid+1
for kid in kids:
    print(kid)
v = z3.IntVal(1)
w = z3.IntVal(1)
print(v.as_long()+w.as_long())
s=z3.Solver()
d=dict()
#print(s.check(10>4))
x = z3.Int('x')
y = x-2
d['v']=x-2
s.add(10>4)
print(s)
print(s.check())
model=s.model()

print(model.eval(x))

# from z3 import *
#
# x = Int('x')
# y = Int('y')
# f = Function('f', IntSort(), IntSort())
# s = Solver()
# s.add(f(f(x)) == x, f(x) == y, x != y)
# print s.check()
# m = s.model()
# print "f(f(x)) =", m.evaluate(f(f(x)))
# print "f(x)    =", m.evaluate(f(x))
# print "f(y)    =", m.evaluate(f(y))
# print "x   =", m.evaluate(x)
# print "y    =", m.evaluate(y)
# print """
# S = DeclareSort('S')       # Declare an uninterpreted sort S
# f = Function('f', S, S)    # Declare function f : S -> S
# x = Const('x', S)          # Declare constant x : S
# """
# sys.stdin.readline()
#
# S = DeclareSort('S')
# f = Function('f', S, S)
# x = Const('x', S)
#
# print """
# s = Solver()               # Create a solver context
# s.add(x == f(f(x)))        # Assert fact 1
# s.add(x == f(f(f(x))))     # Assert fact 2
# """
# sys.stdin.readline()
#
# s = Solver()
# s.add(x == f(f(x)))
# s.add(x == f(f(f(x))))
#
# print """
# print s                   # Print solver's state
# """
# sys.stdin.readline()
# print ">>", s
# sys.stdin.readline()
#
# print """
# print s.check()           # Check satisfiability
# """
# sys.stdin.readline()
# print ">>", s.check()
# sys.stdin.readline()
#
# print """
# s.add(x != f(x))
# print s
# """
#
# s.add(x != f(x))
# sys.stdin.readline()
#
# print ">>", s
# sys.stdin.readline()
#
# print """print s.check()"""
# sys.stdin.readline()
#
# print ">>", s.check()
# sys.stdin.readline()