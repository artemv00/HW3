import main
import unittest
import os
import time


class RuntimeTest(unittest.TestCase):

    def testTimer(self):

        filename = 'temp_test.txt'

        for i in range(1, 50):
            a_list = [int(i) for i in range(1, 1000*i)]
            with open(filename, 'w') as f:
                for x in a_list:
                    f.write(str(x) + ' ')

            st_time = time.time()
            main.body(filename)
            end_time = time.time() - st_time
            with self.subTest(unittest.TestCase):
                self.assertLess(end_time, 1)

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
