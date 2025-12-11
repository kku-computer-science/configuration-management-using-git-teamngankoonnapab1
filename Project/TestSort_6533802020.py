# Project/TestSort.py #653380202-0 Sec4 ธรรมพล สาผิว

import unittest
from QuickSort import quick_sort
from BubbleSort import bubble_sort

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_quick_sort(self):
        data = [8, 7, 2, 1, 0, 9, 6, 5]
        expected = [0, 1, 2, 5, 6, 7, 8, 9]
        
        # ต้องใช้ size = len(data) - 1 สำหรับ high index
        size = len(data)
        quick_sort(data, 0, size - 1)
        
        self.assertEqual(data, expected, "Quick Sort failed to sort correctly")

    def test_bubble_sort(self):
        data = [5, 1, 4, 2, 8]
        expected = [1, 2, 4, 5, 8]
        
        bubble_sort(data)
        
        self.assertEqual(data, expected, "Bubble Sort failed to sort correctly")

    def test_empty_list(self):
        data = []
        expected = []
        
        # Test Quick Sort (ต้องจัดการกรณี size 0)
        quick_sort(data, 0, -1)
        self.assertEqual(data, expected, "Quick Sort failed on empty list")
        
        # Test Bubble Sort
        bubble_sort(data)
        self.assertEqual(data, expected, "Bubble Sort failed on empty list")

if __name__ == '__main__':
    unittest.main()

# วิธีรัน: เปิด Terminal ในโฟลเดอร์ Project แล้วพิมพ์:
# python TestSort.py