import time
a='_'*80
print(f"{a} \n")
str="Sort techniques on dataset"
print(str.center(80))
print(f"\n{a}\n\n")
while True:
          print("Enter \n 1 for bubble sort \n 2 for insertion sort \n 3 for merge sort \n 4 for selection sort")
          cho=int(input("\n Enter the choice"))
          if cho==1:
              start = time.time()
              def bubble_sort(lst):
                 for j in range(len(lst)-1,0,-1):
                     for i in range(j):
                         if lst[i]>lst[i+1]:
                            temp = lst[i]
                            lst[i] = lst[i+1]
                            lst[i+1] = temp
              lst = []
              n=int(input(" \n How many number do you want to enter"))
              for i in range(n):
                 num=int(input(" Enter the number"))
                 lst.append(num)
              bubble_sort(lst)
              print("\n The list after bubble sorting is {}".format(lst))
              end = time.time()
              print(" The time taken by sorting process",end - start)
          if cho==2:
              start = time.time()
              def insertion_sort(lst):
                  for i in range(1,len(lst)):
                      currentvalue = lst[i]
                      position = i
                      while position>0 and lst[position-1]>currentvalue:
                            lst[position]=lst[position-1]
                            position = position-1
                            lst[position]=currentvalue

              lst = []
              n=int(input(" \n How many number do you want to enter:"))
              for i in range(n):
                 num=int(input(" Enter the number:"))
                 lst.append(num)
              insertion_sort(lst)
              print("\n The list after insertion sorting is {}".format(lst))
              end = time.time()
              print(" The time taken by sorting process :",end - start)
          if cho==3:
              start = time.time()
              def mergeSort(alist):
                 if len(alist)>1:
                     mid = len(alist)//2
                     lefthalf = alist[:mid]
                     righthalf = alist[mid:]
                     mergeSort(lefthalf)
                     mergeSort(righthalf)
                     i=0
                     j=0
                     k=0
                     while i < len(lefthalf) and j < len(righthalf):
                          if lefthalf[i] < righthalf[j]:
                             alist[k]=lefthalf[i]
                             i=i+1
                          else:
                               alist[k]=righthalf[j]
                               j=j+1
                          k=k+1
                     while i < len(lefthalf):
                           alist[k]=lefthalf[i]
                           i=i+1
                           k=k+1
                     while j < len(righthalf):
                           alist[k]=righthalf[j]
                           j=j+1
                           k=k+1
              alist = []
              n=int(input(" \n How many number do you want to enter:"))
              for i in range(n):
                 num=int(input(" Enter the number:"))
                 alist.append(num)
              mergeSort(alist)
              print("\n The list after merge sorting is {}".format(alist))
              end = time.time()
              print(" The time taken by sorting process :",end - start)
          if cho==4:
              start = time.time()
              def selection_sort(lst):
                   for fillslot in range(len(lst)-1,0,-1):
                       positionOfMax=0
                       for location in range(1,fillslot+1):
                          if lst[location]>lst[positionOfMax]:
                             positionOfMax = location

                          temp = lst[fillslot]
                          lst[fillslot] = lst[positionOfMax]
                          lst[positionOfMax] = temp
              lst = []
              n=int(input(" \n How many number do you want to enter:"))
              for i in range(n):
                 num=int(input(" Enter the number"))
                 lst.append(num)
              selection_sort(lst)
              print("\n The list after selection sorting is {}".format(lst))
              end = time.time()
              print(" The time taken by sorting process:",end - start)
          n=int(input(" Enter 1 to continue and 0 to exit:"))
          print(" \n \n ")
          if n==0:
             break
