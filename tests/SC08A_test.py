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
        datas.insert(3,{"channel": 2, "speed": 1.0, "scale": 0.0, "exp_val": b'\xe2\x00\x00\x00'})
        datas.insert(4,{"channel": 3, "speed": 1.0, "scale": 1.0, "exp_val": b'\xe3\x00\x01\x00'})
        datas.insert(5,{"channel": 4, "speed": 2.0, "scale": 0.5, "exp_val": b'\xe4\x00\x01\x00'})
        datas.insert(6,{"channel": 5, "speed": 8000.0, "scale": 1.0, "exp_val": b'\xe5}\x00\x00'})
        datas.insert(7,{"channel": 5, "speed": 8001.0, "scale": 1.0, "exp_val": b'\xe5}\x00\x00'})
        for i in datas:
            with self.subTest(i=i):
                self.assertEqual(SC08A.Servo.pack_data(self,
                    i["channel"], #input
                    i["speed"], #input
                    i["scale"],),  #input
                    i["exp_val"]) #output

if __name__=='__main__':
    unittest.main()

