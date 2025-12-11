# Project/MainProgram.py #653380202-0 Sec4 ธรรมพล สาผิว

from Project.QuickSort import quick_sort
from Project.BubbleSort import bubble_sort

def get_input_data():
    """
    รับรายการตัวเลขจากผู้ใช้ และตัวเลือก Algorithm
    """
    try:
        # 1. รับรายการตัวเลข (Input for sort)
        input_str = input("Enter integers to sort (separated by space): ")
        
        # แปลง string ที่รับมาเป็น list ของ integers
        input_list = list(map(int, input_str.split()))

        # 2. รับตัวเลือก Algorithm
        algo_choice = input("Enter sorting algorithm (quick sort / bubble sort): ").lower().strip()
        
        if algo_choice not in ["quick sort", "bubble sort"]:
            print("Invalid algorithm choice. Please choose 'quick sort' or 'bubble sort'.")
            return None, None
            
        return input_list, algo_choice
        
    except ValueError:
        print("Invalid input. Please ensure all inputs are integers.")
        return None, None

def run_sort_program():
    """
    ฟังก์ชันหลักในการเรียกใช้ Sorting Algorithm
    """
    data, choice = get_input_data()
    
    if data is None:
        return

    # สร้างสำเนาของข้อมูลเพื่อป้องกันการแก้ไขข้อมูลต้นฉบับ
    data_to_sort = data.copy()
    
    if choice == "quick sort":
        size = len(data_to_sort)
        # เรียก Quick Sort (ต้องส่ง high และ low index)
        sorted_data = quick_sort(data_to_sort, 0, size - 1)
        print("\n--- Quick Sort Result ---")
        
    elif choice == "bubble sort":
        # เรียก Bubble Sort
        sorted_data = bubble_sort(data_to_sort)
        print("\n--- Bubble Sort Result ---")
        
    print(f"Original Data: {data}")
    print(f"Algorithm Used: {choice.capitalize()}")
    print(f"Sorted Data: {sorted_data}")

# เรียกใช้โปรแกรมเมื่อรันไฟล์ MainProgram.py โดยตรง
if __name__ == "__main__":
    run_sort_program()