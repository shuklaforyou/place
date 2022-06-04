class Solution:
    def sort012(arr,n):
        zero = 0
        one = 0
        two = 0
        for i in arr:
            if i==0:
                zero += 1
            elif i==1:
               one += 1
            else:
                two += 1
        new_arr = zero*[0] + one*[1] + two*[2]
        return new_arr

    if __name__=="__main__":
        n=int(input())
        arr=list(map(int,input().split()))
        print(sort012(arr,n))