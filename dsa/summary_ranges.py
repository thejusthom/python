nums = [0,2,3,4,6,8,9]
i,j = 0,0
output_list = []
while i <len(nums):
    begin_num = nums[j]
    if i!=len(nums)-1 and nums[i] + 1 == nums[i+1]:
        i += 1
    else:
        if nums[i] == begin_num:
            string_to_append = str(begin_num)
            j += 1
        else:
            end_num = nums[i]
            string_to_append = str(begin_num)+"->"+str(end_num)
            j = i
            j += 1
        output_list.append(string_to_append)
        i += 1