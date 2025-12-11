# Project/QuickSort.py #653380202-0 Sec4 ธรรมพล สาผิว

# Project/QuickSort.py

def partition(arr, low, high):
    """
    ฟังก์ชันสำหรับแบ่งส่วน (Partition) โดยเลือกองค์ประกอบสุดท้ายเป็น Pivot
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            # สลับ arr[i] กับ arr[j]
            (arr[i], arr[j]) = (arr[j], arr[i])

    # สลับ Pivot (arr[high]) เข้าสู่ตำแหน่งที่ถูกต้อง (arr[i+1])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    
    # ส่งคืนตำแหน่งของ Pivot
    return i + 1

def quick_sort(arr, low, high):
    """
    ฟังก์ชัน Quick Sort หลัก ที่ใช้การเรียกตัวเองซ้ำ (Recursion)
    """
    if low < high:
        # p เป็นดัชนีของ Pivot ที่ถูกจัดเรียง
        p = partition(arr, low, high)

        # จัดเรียงองค์ประกอบทางซ้าย
        quick_sort(arr, low, p - 1)

        # จัดเรียงองค์ประกอบทางขวา
        quick_sort(arr, p + 1, high)
        
    return arr # เพิ่ม return arr เพื่อให้ MainProgram.py เรียกใช้งานได้ง่าย
