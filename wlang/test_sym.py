# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest
import wlang.ast as ast
import wlang.sym

class TestSym (unittest.TestCase):
    def test_one (self):
        ''' takes short time test <<>>>>while'''
        prg1 = "x:=10; while x <16 do {x:=x+2}; s:=3;while s <= 9 do {s:=s+2}; y:=0 while y >= -9 do {y:=y-3}; q:=10;while q = 4 do {s:=1}; while q < 16 do {q:=q+2};assert x>10"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_four (self):
        ''' takes short time test ???'''
        prg1 = "x:=10; while x > 4 do {x:=x-3};if x>8 then r:=x+7 else r:=x+5;if x<8 then s:=1;if x>=8 then s:=1;if x=8 then s:=1;if x<=8 then s:=1"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
        #   print(result)
        self.assertEquals (len(out), 1)
    def test_two (self):
        ''' takes short time assume and assert'''
        prg1 = "havoc x;assume x > 10;assert x > 15"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result=[]
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
          # print(result)
        self.assertEquals (len(out), 1)
    def test_three (self):
        ''' takes long time test */'''
        prg1 = "havoc x; r:=0;if x>8 then r:=x-7 else r:=x-5; if x>5 then r:=x*2 else r:=x/3"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result=[]
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
         #  print(result)
        self.assertEquals (len(out), 3)
    def test_six (self):
        ''' takes long time test */'''
        prg1 = "havoc x; r:=0;if x<=8 then r:=x-7 else r:=x-5; if x>=5 then r:=x*2 else r:=x/3"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result=[]
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
          # print(result)
        self.assertEquals (len(out), 3)

    def test_seven(self):
        ''' takes long time test */'''
        prg1 = "havoc x; r:=0;if x=8 then r:=x-7 else r:=x-5; if x<5 then r:=x*2 else r:=x/3"
        ast1 = ast.parse_string(prg1)
        sym = wlang.sym.SymExec()
        st = wlang.sym.SymState()
        out = [s for s in sym.run(ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
            #print(result)
        self.assertEquals(len(out), 3)
    def test_five (self):
        ''' takes long time test <=>= in if'''
        prg1 = "x:=10; if x>8 then r:=x-7 else r:=x-5;if x>10 then r:=x-7;if x<=5 then r:=x-7;if x<=10 then r:=x-7 else r:=x-5;if x>=12 then r:=x-7;if x>=8 then r:=x-7 else r:=x-5;if x<12 then r:=x-7;if x<8 then r:=x-7 else r:=x-5;if x=10 then r:=x-7;if x=8 then r:=x-7 else r:=x-5"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                print(state.__repr__())
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
           #print(result)
        self.assertEquals (len(out), 1)
    def test_eight (self):
        ''' takes short time test assert ><=<>'''
        prg1 = "havoc x,y,z,e; if x > 4 then assert x<2 else assert x<5;if y > 4 then assert y>2 else assert y>=5;if z > 1 then assert z<=2 else assert z=5"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
           #print(result)
        self.assertEquals (len(out), 1)
    def test_nine (self):
        ''' takes ??? time test assume '''
        prg1 = "havoc x,y,z,e; assume x>10;assume y<5;assume x<=20;assume y>=2;assume z=1;skip;print_state"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
           #print(result)
        self.assertEquals (len(out), 1)
    def test_ten (self):
        ''' takes short time test and or not in while'''
        prg1 = "x := 10; { p := 25; x := 1; n := 5 };  if not x>=n and p>n or x<p then p :=10 ;if true then x:=1;if false then y:=1 else y:=-1 ;if false then y:=1"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
           #print(result)
        self.assertEquals (len(out), 1)
    def test_eleven (self):
        ''' takes short ime test not '''
        prg1 = "x := 10; { p := 25; x := 1; n := 5 };  if not x>n then p :=10 "
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
           #print(result)
        self.assertEquals (len(out), 1)
    def test_12 (self):
        ''' takes long time test > in while'''
        prg1 = "havoc x; while x > 4 do {p:=1}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_13 (self):
        ''' takes long time test <><=>= = in while'''
        prg1 = "havoc x,y,s,q; while x <16 do {x:=x+2}; s:=3;while s <= 9 do {s:=s+2}; y:=0 while y >= -9 do {y:=y-3}; q:=10;while q = 4 do {s:=1}; while q < 16 do {q:=q+2};assert x>10"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 11)

    def test_14(self):
        ''' takes long time test if and <><= >= ='''
        prg1 = "havoc x; if 8<x then r:=x-7 else r:=x-5;if 10>x then r:=x-7;if 5>=x then r:=x-7;if x<=10 then r:=x-7 else r:=x-5;if 12<=x then r:=x-7;if x>=8 then r:=x-7 else r:=x-5;if x<12 then r:=x-7;if x<8 then r:=x-7 else r:=x-5;if 10=x then r:=x-7;if x=8 then r:=x-7 else r:=x-5"
        ast1 = ast.parse_string(prg1)
        sym = wlang.sym.SymExec()
        st = wlang.sym.SymState()
        out = [s for s in sym.run(ast1, st)]
        list_result = []
        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
                result = state.pick_concerete()
                list_result.append(result)
            print ('[symexec]: found', count, 'symbolic states')
        #for result in list_result:
            #print(result)
        self.assertEquals(len(out), 7)
    def test_15 (self):
        ''' takes long time test = in while in 1 state'''
        prg1 = "havoc x; while x = 4 do {p:=1}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_16 (self):
        ''' takes long time test >= in 1 state'''
        prg1 = "havoc x; while x >= 4 do {p:=1}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_18 (self):
        ''' takes short time test >= in while'''
        prg1 = "x:=10; while x >= 4 do {x:=x-2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_19 (self):
        ''' takes short time test >= in while'''
        prg1 = "x:=10; while x >= 12 do {x:=x+2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_20 (self):
        ''' = while concrete'''
        prg1 = "x:=10; while x=10 do {x:=x+2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_21 (self):
        ''' concrete <= and while '''
        prg1 = "x:=4; while x<=10 do {x:=x+2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_22 (self):
        ''' takes long time test <= in while with 11 states'''
        prg1 = "havoc x; while x<=10 do {x:=x+2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 11)
    def test_23 (self):
        ''' takes long time test <= in while with 1 state'''
        prg1 = "havoc x; while x<=10 do {x:=x-2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    def test_24 (self):
        prg1 = "x:=16; while x<=10 do {x:=x-2}"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]

        if out is None:
            print ('[symexec]: no output states')
        else:
            count = 0
            for state in out:
                count = count + 1
                print ('[symexec]: symbolic state reached')
                #print (state)
            print ('[symexec]: found', count, 'symbolic states')
        self.assertEquals (len(out), 1)
    # def test_eight (self):
    #     ''' takes short time test assert ><=<>'''
    #     prg1 = "havoc x,y,z,e; while x<=10 do {x:=x+2};if x > 4 then p:=1 else p:=1;if y > 4 then p:=1 else p:=1;if z > 1 then p:=1 else p:=1"
    #     ast1 = ast.parse_string (prg1)
    #     sym = wlang.sym.SymExec ()
    #     st = wlang.sym.SymState ()
    #     out = [s for s in sym.run (ast1, st)]
    #     list_result = []
    #     if out is None:
    #         print ('[symexec]: no output states')
    #     else:
    #         count = 0
    #         for state in out:
    #             count = count + 1
    #             print ('[symexec]: symbolic state reached')
    #             #print (state)
    #             result = state.pick_concerete()
    #             list_result.append(result)
    #         print ('[symexec]: found', count, 'symbolic states')
    #     #for result in list_result:
    #     #   print(result)
    #     self.assertEquals (len(out), 44)
    # def test_eight (self):
    #     ''' takes short time test assert ><=<>'''
    #     prg1 = "havoc x,y,z,e; while x<=10 do {x:=x+2};if x > 4 then p:=1 else p:=1;if y > 4 then p:=1 else p:=1;if z > 1 then p:=1 else p:=1;while y<=10 do {y:=y+2};if e > 1 then p:=1 else p:=1"
    #     ast1 = ast.parse_string (prg1)
    #     sym = wlang.sym.SymExec ()
    #     st = wlang.sym.SymState ()
    #     out = [s for s in sym.run (ast1, st)]
    #     list_result = []
    #     if out is None:
    #         print ('[symexec]: no output states')
    #     else:
    #         count = 0
    #         for state in out:
    #             count = count + 1
    #             print ('[symexec]: symbolic state reached')
    #             #print (state)
    #             result = state.pick_concerete()
    #             list_result.append(result)
    #         print ('[symexec]: found', count, 'symbolic states')
    #     #for result in list_result:
    #     #   print(result)
    #     self.assertEquals (len(out), 242)
    # def test_22 (self):
    #     ''' takes long time test <= in while with 11 states'''
    #     prg1 = "havoc x; while x<=10 do {x:=x+2}"
    #     ast1 = ast.parse_string (prg1)
    #     sym = wlang.sym.SymExec ()
    #     st = wlang.sym.SymState ()
    #     out = [s for s in sym.run (ast1, st)]
    #
    #     if out is None:
    #         print ('[symexec]: no output states')
    #     else:
    #         count = 0
    #         for state in out:
    #             count = count + 1
    #             print ('[symexec]: symbolic state reached')
    #             #print (state)
    #         print ('[symexec]: found', count, 'symbolic states')
    #     self.assertEquals (len(out), 11)
    # def test_eight (self):
    #     ''' takes short time test assert ><=<>'''
    #     prg1 = "havoc x,y,z,e; while x<=10 do {x:=x+2};if x > 4 then p:=1 else p:=1;if y > 4 then p:=1 else p:=1;if z > 1 then p:=1 else p:=1;if e > 1 then p:=1 else p:=1"
    #     ast1 = ast.parse_string (prg1)
    #     sym = wlang.sym.SymExec ()
    #     st = wlang.sym.SymState ()
    #     out = [s for s in sym.run (ast1, st)]
    #     list_result = []
    #     if out is None:
    #         print ('[symexec]: no output states')
    #     else:
    #         count = 0
    #         for state in out:
    #             count = count + 1
    #             print ('[symexec]: symbolic state reached')
    #             #print (state)
    #             result = state.pick_concerete()
    #             list_result.append(result)
    #         print ('[symexec]: found', count, 'symbolic states')
    #     #for result in list_result:
    #     #   print(result)
    #     self.assertEquals (len(out), 44)