import z3
## See https://en.wikipedia.org/wiki/Verbal_arithmetic
## cute: http://mathforum.org/library/drmath/view/60417.html

vars = dict()
character=None
def _mk_int_var (x):
    # print("this is in mkintvar"+x)
    if x not in vars:
        vars[x] = z3.Int (str(x))
    return vars[x]

def mk_var (x):
    return _mk_int_var (x)

def get_vars ():
    return vars.values ()

def get_list(string1):
    equation=[]
    size1 = len(list(string1)) - 1
    for s in list(string1):
        equation.append(vars[s] * 10 ** size1)
        size1 = size1 - 1
    return equation
def solve (s1, s2, s3):
    global vars
    vars = dict()
    vars1 = dict()
    solver = z3.Solver()
    i=0
    for s in list(s1):
        exp=mk_var(s)
        i=i+1
        if i==1:
            solver.add(0<exp,exp<=9)
        else:
            solver.add(0<=exp,exp<=9)
    i = 0
    for s in list(s2):
        exp=mk_var(s)
        i = i + 1
        if i == 1:
            solver.add(0<exp,exp<=9)
        else:
            solver.add(0<=exp,exp<=9)
    i=0
    for s in list(s3):
        exp=mk_var(s)
        i = i + 1
        if i == 1:
            solver.add(0<exp,exp<=9)
        else:
            solver.add(0<=exp,exp<=9)
    # print("this is in solve")
    # print(vars)
    newVars=vars.copy()
    list1=get_list(s1)
    list2=get_list(s2)
    list3=get_list(s3)
    for x in range(0,len(vars.values())):
        for y in range(1,len(vars.values())):
            if x!=y:
                solver.add(z3.Distinct(vars.values()[x],vars.values()[y]))
    # print("this is in list")
    # print(list1)
    # print(list2)
    for v in vars:
        s=mk_var(v)
        # print(s)
    # Replace with your solution
    x = z3.Int('x')
    y = z3.Int('y')


    # print x
    # print("this is lambda")
    x = reduce(lambda x, y: x + y, list1)
    y = reduce(lambda x, y: x + y, list2)
    z = reduce(lambda x, y: x + y, list3)
    solver.add(x+y==z)


    # print solver
    # print "Solving constraints in the solver s ..."
    # print type(solver.check())
    # print solver.check()
    if solver.check() == z3.unsat:
        return None
    m = solver.model()
    # res=[]
    # print m
    str1=0
    for s in list1:
        str1=str1+m.eval(s).as_long()
    str2=0
    for s in list2:
        str2=str2+m.eval(s).as_long()
    str3=0
    for s in list3:
        str3=str3+m.eval(s).as_long()
    res=(str1,str2,str3)
    return res
    # print "S = %s" % m[newVars['M']]
    # print "Create a new scope..."
    # solver.push()
    # solver.add(y < 11)
    # print solver
    # print "Solving updated set of constraints..."
    # print solver.check()
    #
    # print "Restoring state..."
    # solver.pop()
    # print solver
    # print "Solving restored set of constraints..."
    # print solver.check()
    # pass


def print_sum (s1, s2, s3):
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    print s1.rjust (len(s3) + 1)
    print '+'
    print s2.rjust (len(s3) + 1)
    print ' ' + ('-'*(len(s3)))
    print s3.rjust (len(s3) + 1)
    
def puzzle (s1, s2, s3):
    print_sum (s1, s2, s3)
    res = solve (s1, s2, s3)
    if res is None:
        print 'No solution'
    else:
        print 'Solution:'
        print_sum (res[0], res[1], res[2])
        
if __name__ == '__main__':
    puzzle ('SEND', 'MORE', 'MONEY')
