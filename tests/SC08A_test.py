import unittest
import sys
sys.path.append("..")
import SC08A

class TestConvToBin(unittest.TestCase):

    #data to test [channel, speed, scale, expected value]
    #TODO add subtest

    def test_pack_data(self):
        datas=[]
        datas.insert(0,{"channel": 0, "speed": 0.0, "scale": 0.0, "exp_val": b'\xe0\x00\x00\x00'})
        datas.insert(1,{"channel": 1, "speed": 0.0, "scale": 0.0, "exp_val": b'\xe1\x00\x00\x00'})
        datas.insert(2,{"channel": 8, "speed": 0.0, "scale": 0.0, "exp_val": b'\xe8\x00\x00\x00'})
        datas.insert(3,{"channel": 2, "speed": 2001.1, "scale": 0.0, "exp_val": b'\xe2\x00\x00\x00'})
        for i in datas:
            with self.subTest(i=i):
                self.assertEqual(SC08A.Servo.pack_data(self,
                    i["channel"], #input
                    i["speed"], #input
                    i["scale"],),  #input
                    i["exp_val"]) #output
                print (i["speed"]) 

if __name__=='__main__':
    unittest.main()

