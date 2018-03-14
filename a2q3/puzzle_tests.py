import unittest
from a2q3.verbal_arithmetic import solve

class PuzzleTests (unittest.TestCase):

    def setUp (self):
        """Reset Z3 context between tests"""
        import z3
        z3._main_ctx = None
    def tearDown (self):
        """Reset Z3 context after test"""
        import z3
        z3._main_ctx = None
        
    def test_1 (self):
        """SEND + MORE = MONEY"""
        a,b,c = solve ('SEND', 'MORE', 'MONEY')
        print a,b,c
        # self.assertEquals (res, (9567, 1085, 10652))

    # def test_2 (self):
    #     res = solve('ABC', 'EGD', 'THREE')
    #     self.assertEquals(res, None)
    #
    # def test_3 (self):
    #     res = solve('PLAY', 'THE', 'GAME')
    #     self.assertEquals(res, (6320, 894, 7214))
    #
    # def test_4 (self):
    #     res = solve('BEAT', 'THE', 'DRUME')
    #     self.assertEquals(res, None)
        
