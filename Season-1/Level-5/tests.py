import unittest
import code as c

class TestCrypto(unittest.TestCase): 
  
    # verifies that hash and verification are matching each other for SHA
    def test_1(self):
        rd = c.Random_generator()
        hasher = c.Hasher()
        pass_ver = hasher.password_verification("abc", hasher.password_hash("abc",rd.generate_salt()))
        self.assertEqual(pass_ver, True)
        
if __name__ == '__main__':    
    unittest.main()