
class Solution:
    def rotate(self, nums, k):
        for i in range(0, k, 1):
            #print(i)
            nums_new = [0]*len(nums)
            for j in range(0, len(nums), 1):
                if (j == len(nums)-1):
                    nums_new[0]   = nums[j]
                else:
                    nums_new[j+1] = nums[j]
            nums[:] = nums_new
            del nums_new
            print(nums)

n = len(nums)
k %= n
k = k%n

x %= 3
x = x % 3


class Solution:
    def rotate(self, nums, k):
        for i in range(0, k, 1):
            previous = nums[-1]
            for j in range(0, len(nums), 1):
                nums[j], previous = previous, nums[j]

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(0, n, 1):
            a[(i + k)% n] = nums[i]
        nums[:] = a


nums = [1,2,3,4,5,6,7]
k = 3

answer = Solution()
answer.rotate(nums,k)
print(nums)


sol.rotate(nums,k)
print(nums)



nums = [-1,-100,3,99]
k = 2


for j in range(0, k, 1):
    print(j)
    nums_new = nums.copy()
    for n in range(0, len(nums), 1):
        if (n == len(nums)-1):
            nums_new[0]   = nums[n]
        else:
            nums_new[n+1] = nums[n]
    nums = nums_new.copy()
    print(nums)
    
nums    
nums_new    
    


class Solution:
    def maxProfit(self, prices):
        profit = 0
        price_start = prices[0]
        for i in range(0, len(prices)-1, 1):
            if   (prices[i+1] >= prices[i]): # prices is going up
                price_end   = prices[i+1]
            elif (prices[i+1] <  prices[i]): # prices is going down
                price_start = prices[i+1]
                delta = price_end - price_start
                profit = profit + delta
                print(profit)
        return(profit)
    
prices = [7,6,4,3,1]
answer = Solution()
answer.maxProfit(prices)


prices = [7,1,5,3,6,4]

profit = 0
price_start = prices[0]
price_end   = 0
i = 0
for i in range(0, len(prices)-1, 1):
    if   (prices[i+1] > prices[i]): # price is going up
        profit = profit + (prices[i+1] - prices[i])



public class Solution {
public int maxProfit(int[] prices) {
    int total = 0;
    for (int i=0; i< prices.length-1; i++) {
        if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
    }
    
    return total;
}




prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) an

prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no tra

prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at th


profit = 0
price_start = prices[0]
price_end   = 0
i = 0
for i in range(0, len(prices)-1, 1):
    print('  i %s ' %(i))
    print('    start %s end %s ' %(price_start, price_end))
    print('    prices %s -> %s ' %(prices[i], prices[i+1]))
    if   (prices[i+1] >= price_start): # price is going up
        price_end   = prices[i+1]
        print ('    set price_end')
    elif (prices[i+1] <  price_start): # prices is going down
        if (i > 0):
            if (price_end > price_start):
                delta = price_end - price_start
                profit = profit + delta
                print('  taking profit of %s delta ' %(delta))
        price_start = prices[i+1]
        print ('  set price_start')





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



    