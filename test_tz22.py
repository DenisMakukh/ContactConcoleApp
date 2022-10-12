import unittest
import stepik

from functools import reduce

class Testing(unittest.TestCase):
    if len(stepik.sp1) != 0:
        def test_min(self):
            answer = stepik._min(stepik.sp1)
            self.assertEqual(answer, min(stepik.sp1))
        def test_max(self):
            answer2 = stepik._max(stepik.sp1)
            self.assertEqual(answer2, max(stepik.sp1))
        def test_sum(self):
            answer3 = stepik._sum(stepik.sp1)
            self.assertEqual(answer3, sum(stepik.sp1))
        def test_mult(self):
            answer4 = stepik._mult(stepik.sp1)
            self.assertEqual(answer4, reduce((lambda x,y: x * y), stepik.sp1))
        def test_my(self):
            answer5 = stepik._max(stepik.sp1) * stepik._min(stepik.sp1)
            self.assertEqual(answer5, max(stepik.sp1) * min(stepik.sp1))
    else:
        def test_min1(self):
            answer6 = stepik._min(stepik.sp1)
            self.assertEqual(answer6, None)
        def test_max1(self):
            answer7 = stepik._max(stepik.sp1)
            self.assertEqual(answer7, None)
        def test_sum1(self):
            answer8 = stepik._sum(stepik.sp1)
            self.assertEqual(answer8, None)
        def test_mult1(self):
            answer9 = stepik._mult(stepik.sp1)
            self.assertEqual(answer9, None)
        def test_my1(self):
            answer10 = stepik.minef(stepik.sp1)
            self.assertEqual(answer10, None)
    def test_Time(self):
        print('Время работы программы:', stepik.c.microseconds, 'микросекунд', 'или', stepik.c.microseconds / 1000000, 'секунд')
if __name__ == '__main__':
    unittest.main()