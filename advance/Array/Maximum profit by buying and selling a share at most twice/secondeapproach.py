if __name__ == '__main__':
    price = [ 2, 30, 15, 10, 8, 25, 80] 
    n = 7
 
    # adding array
    profit = 0
 
    # Initializing variable
    # valley-peak approach
    '''
                       80
                       /
        30            /
       /  \          25
      /    15       /
     /      \      /
    2        10   /
               \ /
                8
     '''
    for i in range(1,n):
 
        # traversing through array from (i+1)th
        # position
        sub = price[i] - price[i - 1]
        if (sub > 0):
            profit += sub
     
 
    print("Maximum Profit=" ,profit)

    # Algorithmic Paradigm: Dynamic Programming 

    # . For example, if price [] = {2, 4, 2, 4, 2, 4} then this particular 
    # approach will give result 6 while in this given problem you can only 
    # do two transactions so answer should be 4. Hence this approach only 
    # works when we have a chance to do infinite transaction. 


#The time and space complexity is O(n) and O(1) respectively.
 