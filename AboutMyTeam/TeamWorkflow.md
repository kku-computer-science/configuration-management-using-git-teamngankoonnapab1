ส่วนที่ 1: การตั้งค่าโครงสร้างหลัก (Branch main)

1 Clone Repo,Clone Team Repository มาที่ Local
2 สร้างโครงสร้าง,สร้าง Folder AboutMyTeam และ Project,$ mkdir AboutMyTeam Project
3 สร้างไฟล์ทีม,สร้างและแก้ไข AboutMyTeam/TeamWorkflow.md,$ touch AboutMyTeam/TeamWorkflow.md
4 Commit โครงสร้าง,Stage และ Commit โครงสร้างหลัก,"$ git add . / $ git commit -m ""Created TeamWorkflow.md..."""
5 Push โครงสร้าง,Push งานขึ้น Branch main,$ git push origin main

ส่วนที่ 2: การทำงานส่วนตัว (สร้าง 3 Branches จำลอง)

A: Quick Sort	Thammaphon_xxxx	
6. สร้าง Branch	$ git checkout -b 	
7. Implement Code	สร้าง Project/QuickSort.py, Project/
8. Commit & Push	$ git add Project/ / $ git commit -m "Quick Sort..." / $ git push origin 	

B: Bubble Sort	B_xxxx	
9. สลับ/สร้าง Branch	$ git checkout main / $ git checkout -b 
10. Implement Code	สร้าง Project/BubbleSort.py, Project/	
11. Commit & Push	$ git add Project/ / $ git commit -m "Bubble Sort..." / $ git push origin 	

C: Main Program	C_xxxx	
12. สลับ/สร้าง Branch	$ git checkout main / $ git checkout -b 
13. Implement Code	สร้าง Project/MainProgram.py, Project/
14. Commit & Push	$ git add Project/ / $ git commit -m "Main Program..." / $ git push origin 

ส่วนที่ 3: การรวมงาน (Merge) และส่งมอบงานสุดท้ายส่วนที่ 3: การรวมงาน (Merge) และส่งมอบงานสุดท้าย
15. สลับไป main	สลับไป Branch หลักและ Pull งานล่าสุด	$ git checkout main / $ git pull origin main
16. Merge งาน A	รวมงาน Quick Sort เข้าสู่ main	$ git merge 
17. Merge งาน B	รวมงาน Bubble Sort เข้าสู่ main	$ git merge 
18. Merge งาน C	รวมงาน Main Program เข้าสู่ main	$ git merge 
19. แก้ไข Conflict	หากเกิด Conflict ให้แก้ไขไฟล์และ Commit การแก้ไข	$ git status / (แก้ไขไฟล์) / $ git add . / $ git commit
20. Push งานสุดท้าย	Push Branch main ที่สมบูรณ์แล้วขึ้น Remote	$ git push origin main

