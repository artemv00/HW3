import main
import math
import unittest
import random
import os


class FooCorrection(unittest.TestCase):

    # Тесты корректности определения минимума, максимума, суммы и произведения функций

    def testMin(self):
        for i in range(5):
            tst_arr = [int(i * random.random()) for i in range(-1000, 1000)]
            with self.subTest():
                self.assertEqual(min(tst_arr), main.minimum(tst_arr))

    def testMax(self):
        for i in range(5):
            tst_arr = [int(i * random.random()) for i in range(-1000, 1000)]
            with self.subTest():
                self.assertEqual(max(tst_arr), main.maximum(tst_arr))

    def testSum(self):
        for i in range(5):
            tst_arr = [int(i * random.random()) for i in range(1, 1000)]
            with self.subTest():
                self.assertEqual(sum(tst_arr), main.addition(tst_arr))

    def testMult(self):
        for i in range(5):
            tst_arr = [int(i * random.random()) for i in range(1, 1000)]
            with self.subTest():
                self.assertEqual(math.prod(tst_arr), main.multiplication(tst_arr))


# Дополнительные тесты

class AdditionalTests(unittest.TestCase):

    # Тесты на случай пустого файла

    def testMinIfEmpty(self):
        tst_array = []
        self.assertEqual(None, main.minimum(tst_array))

    def testMaxIfEmpty(self):
        tst_array = []
        self.assertEqual(None, main.maximum(tst_array))

    def testSumIfEmpty(self):
        tst_array = []
        self.assertEqual(None, main.addition(tst_array))

    def testMultIfEmpty(self):
        tst_array = []
        self.assertEqual(None, main.minimum(tst_array))


class ExpectedFailureTest(unittest.TestCase):

    @unittest.expectedFailure
    def testFileReaderError(self):
        with open('temp_file.txt', 'w') as f:
            for i in [1, 2, 'a']:
                f.write(str(i) + ' ')
        self.assertTrue(main.file_reader('temp_file.txt'))

    @unittest.expectedFailure
    def testMinIfStr(self):
        os.remove('temp_file.txt')
        tst_array = [1, 2, 3, 'a']
        self.assertEqual(min(tst_array), main.minimum(tst_array))

    @unittest.expectedFailure
    def testMaxIfStr(self):
        tst_array = [1, 2, 3, 'a']
        self.assertEqual(max(tst_array), main.maximum(tst_array))

    @unittest.expectedFailure
    def testSumIfStr(self):
        tst_array = [1, 2, 3, 'a']
        self.assertEqual(sum(tst_array), main.addition(tst_array))

    # Следующий тест должен выполнится, но оставил (возможно захочу модернизировать код и мне нужна ошибка тут)
    @unittest.skip
    def testMultIfStr(self):
        tst_array = [1, 2, 3, 'a']
        self.assertEqual(math.prod(tst_array), main.multiplication(tst_array))


if __name__ == '__main__':
    unittest.main()
