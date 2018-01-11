# Author : John Tsang
# Date   : January 11, 2018
# Purpose: random draw from sample (with replacement and without replacement) 
def random_sampling(sample, size, is_replacement = True):
    import random
    len_sample = len(sample)
    if (len_sample <= 0):
        raise ValueError('Size of sample must be greater than or equal to 1.')
    if (is_replacement == True):
        rt_lst = [random.choice(sample) for index in range(0,size)]
        return rt_lst
    else:
        if (size > len_sample):
            raise ValueError('size must be less than or equal to size of sample for without replacement.')
        rt_lst = []
        for index in range(0,size):
            draw = random.choice(sample)
            sample.remove(draw)
            rt_lst.append(draw)
        return rt_lst
