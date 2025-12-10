# Project/QuickSort.py #653380202-0 Sec4 ธรรมพล สาผิว

def partition(arr, low, high):
    """
    ฟังก์ชันสำหรับแบ่งส่วน (Partition) โดยเลือกองค์ประกอบสุดท้ายเป็น Pivot
    และจัดเรียงองค์ประกอบที่เล็กกว่า Pivot ให้อยู่ทางซ้าย
    """
    pivot = arr[high]  # กำหนดองค์ประกอบสุดท้ายเป็น Pivot
    i = low - 1        # ตัวชี้สำหรับองค์ประกอบที่เล็กกว่า

    for j in range(low, high):
        # ถ้าองค์ประกอบปัจจุบันมีค่าน้อยกว่าหรือเท่ากับ Pivot
        if arr[j] <= pivot:
            # เพิ่มตัวชี้ขององค์ประกอบที่เล็กกว่า
            i = i + 1
            # สลับ arr[i] กับ arr[j]
            (arr[i], arr[j]) = (arr[j], arr[i])

    #สลับ Pivot เข้าสู่ตำแหน่งที่ถูกต้อง (arr[i + 1] กับ arr[high])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1]) 
    
    # ส่งคืนตำแหน่งของ Pivot
    return i + 1
