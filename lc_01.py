
#class adderClass(object):
#     def __init__(self, data):
#         self.data = data
#     def scan(self):
#         print(self.data)
#    def sigmoid(self, data):
#        g = data + 4
#        return (g)


class Solution1:
    def removeDuplicates(self, nums):    
        x = 1
        for i in range(len(nums)-1):
         	if (nums[i] != nums[i+1]):
                 nums[x] = nums[i+1]
                 x = x+1
        #return(x, nums[0:x])        
        return(x)        


class Solution2:
    def removeDuplicates(self, nums):
        count = 0
        i = 0
        while i < len(nums):
            if count >= 2:
                if len(nums) - i > 1 and nums[i] != nums[i+1]:
                    count = 0
                nums.remove(nums[i])
            else:
                    if len(nums) - i > 1 and nums[i] == nums[i+1]:
                        count += 1
                    else:
                        count = 0
                    i += 1
        return (len(nums))


#nums = [0, 1, 2, 3, 4, 4, 4]
nums = [1, 1, 2]

answer1 = Solution1()

nums[0:x]
nums
n_elements = answer1.removeDuplicates(nums)
print(n_elements)
print(nums[0:n_elements])


nums = [1, 1, 2]
answer2 = Solution2()
n_elements = answer2.removeDuplicates(nums)
print(n_elements)
print(nums[0:n_elements])


Solution1(nums).remove_duplicates()
Solution2(nums).remove_duplicates()



nums.removeDuplicates()

nums.remove_duplicate
nums.remove_duplicate()

remove_duplicate(nums)


# class Solution:
#     def __init__(self):
#         self.removeDuplicates = removeDuplicates
    
#     #def removeDuplicates(self, nums: list[int]) -> int:
#     def removeDuplicates(nums):
#         length = 0
#         if len(nums) == 0: 
#             return length
#         for i in range(1, len(nums)):
#             if nums[length] < nums[i]:
#                 length += 1
#                 nums[length] = nums[i]
#         return length+1



# class Shark:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def swim(self):
#         # Reference the name
#         print(self.name + " is swimming.")

#     def be_awesome(self):
#         # Reference the name
#         print(self.name + " is being awesome.")



# def main():
#     sammy = Shark('Sammy', 5)
#     sammy.swim()
#     sammy.be_awesome()

# if __name__ == "__main__":
#     main()



    