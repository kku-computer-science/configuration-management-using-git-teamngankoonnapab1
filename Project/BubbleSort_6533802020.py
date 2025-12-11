# Project/BubbleSort.py #653380202-0 Sec4 ธรรมพล สาผิว

def bubble_sort(arr):
    """
    ฟังก์ชัน Bubble Sort Algorithm
    """
    n = len(arr)
    # วนลูป n-1 รอบ
    for i in range(n - 1):
        # วนลูปเพื่อเปรียบเทียบคู่ที่อยู่ติดกัน
        for j in range(0, n - i - 1):
            # เปรียบเทียบและสลับถ้าองค์ประกอบด้านซ้ายใหญ่กว่าด้านขวา
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr # คืนค่ารายการที่ถูกเรียงแล้ว