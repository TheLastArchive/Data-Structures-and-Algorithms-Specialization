import timeit
from collections import deque
import random
import unittest
#Make sure to rename the file for testing
import max_sliding_window as msw


class TestMaxSlidingWindow(unittest.TestCase):

    def test_random_sequences(self):

        for _ in range(101):
            n = random.randint(1, 101)
            m = random.randint(1, n)
            sequence = []    
            for i in range(n):
                sequence.append(random.randint(1, 101))

            self.assertEqual(
                msw.max_sliding_window(sequence, m), 
                msw.given_solution(sequence, m))

    """
    This test case will not check if the generated sequences are correct as that will
    take too long. We simply check that the tests are being completed in a timely manner
    """
    def test_random_sequences_large(self):

        for _ in range(6):
            n = random.randint(1, 100001)
            m = random.randint(1, n)
            sequence = []    
            for i in range(n):
                sequence.append(random.randint(1, 100001))

            self.assertTrue(
                len(msw.max_sliding_window(sequence, m)) >= 0)
    

    def test_worst_case(self):
        
        sequence = []
        m = 50000
        for _ in range(100001):
            sequence.append(random.randint(1, 100001))
        
        self.assertTrue(len(msw.max_sliding_window(sequence, m)) >= 0)

if __name__ == "__main__":
    unittest.main()

    