import unittest, os

class TestExamples(unittest.TestCase):

    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.expath = os.path.normpath(dir_path + "/../examples")

    def assertAlmostEqualLists(self,L1,L2,places=7):
        self.assertEqual(len(L1),len(L2))
        for u,v in zip(L1,L2): self.assertAlmostEqual(u,v,places)

    ## examples/doc/chap8 scripts

    def test_ch8_conelp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/conelp.py'),gdict)
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_coneqp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/coneqp.py'),gdict)
        self.assertAlmostEqualLists(gdict['x'],[0.72558319,0.61806264,0.30253528],5)

    def test_ch8_lp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/lp.py'),gdict)
        self.assertTrue(gdict['sol']['status'] is 'optimal')
        self.assertAlmostEqualLists(list(gdict['sol']['x']),[1.0,1.0],5)

    def test_ch8_socp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/socp.py'),gdict)
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_sdp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/sdp.py'),gdict)
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_mcsdp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/mcsdp.py'),gdict)
        n = gdict['n']
        z = +gdict['z']
        self.assertAlmostEqualLists(list(z[::n+1]),n*[1.0],5)

    def test_ch8_l1(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/l1.py'),gdict)
        P,x,y = gdict['P'],gdict['x'],gdict['y']
        self.assertAlmostEqualLists(list(P.T*y),P.size[1]*[0.0],5)

    def test_ch8_l1regls(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap8/l1regls.py'),gdict)

    ## examples/doc/chap9 scripts

    def test_ch9_gp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap9/gp.py'),gdict)

    def test_ch9_acent(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap9/acent.py'),gdict)

    def test_ch9_acent2(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap9/acent2.py'),gdict)

    def test_ch9_l2ac(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap9/l2ac.py'),gdict)

    ## examples/doc/chap10 scripts

    def test_ch10_lp(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap10/lp.py'),gdict)

    def test_ch10_acent2(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap10/roblp.py'),gdict)

    def test_ch10_l2ac(self):
        gdict = dict()
        execfile(os.path.join(self.expath,'doc/chap10/l1svc.py'),gdict)

if __name__ == '__main__':
    unittest.main()
