import unittest

 
class TestUM(unittest.TestCase):
 
    def test_figures(self):
        self.assertEqual( open("fig1.png","rb").read(), open("plot1.png","rb").read() )
        self.assertEqual( open("fig2.png","rb").read(), open("plot2.png","rb").read() )
        self.assertEqual( open("fig3.png","rb").read(), open("plot3.png","rb").read() )