import heapq
# heap=[]
# heapq.heappush(heap,10)
# heapq.heappush(heap,20)
# heapq.heappush(heap,1)
# print(heap)
# heapq.heappop(heap)
# print(heap)
# heapq.heappushpop(heap,5)
# print(heap)

list1=[1,2,3,4,5,6,7,8,9]
heapq.heapify(list1)
print(list1)
heapq.heapreplace(list1,100)
print(list1)
print(heapq.nsmallest(2,list1))
print(heapq.nlargest(2,list1))