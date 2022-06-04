import heapq
list1=[(1,"ria"),(4,"sia"),(3,"gia")]
print(list1)
heapq.heapify(list1)
for i in  range(len(list1)):
    print(heapq.heappop(list1)) 

# preority queue in heap  