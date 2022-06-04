def maxsubarraysum(a,size):
    max_so_far=a[0]
    max_ending_here =0
    for i in range(0,size):
        max_ending_here=max_ending_here+ a[i]

        # max_ending_here not contain negative element this contain than become 0
        if max_ending_here<0:
            max_ending_here=0
        # do not compare for all elements.comapore only
        #   when max_ending_here >0

        elif (max_so_far<max_ending_here):
            max_so_far=max_ending_here

        return max_so_far

