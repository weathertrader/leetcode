#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:26:51 2020

@author: csmith
"""
import collections

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    #pattern 3 - works
    def findMode(self, root):
        count = collections.defaultdict(int)
        self.dfs(root, count)
        print(count)
        max_count = max(count.values())
        print(max_count)
        result = [key for key, value in count.items() if value == max_count]
        return result
    def dfs(self, node, count):
        if not node:
            return
        count[node.val] += 1
        self.dfs(node.left, count)
        self.dfs(node.right, count)

    #pattern 2b works
    def findMode(self, root):
        def dfs(node, count):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left, count)
            dfs(node.right, count)
        count = collections.defaultdict(int)
        dfs(root, count)
        print(count)
        max_count = max(count.values())
        print(max_count)
        result = [key for key, value in count.items() if value == max_count]
        return result

    #pattern 2a works
    def findMode(self, root):
        count = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(count)
        max_count = max(count.values())
        print(max_count)
        result = [key for key, value in count.items() if value == max_count]
        return result

    # pattern 1 - preferred 
    def findMode(self, root):
        self.count = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return
            self.count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(self.count)
        max_count = max(self.count.values())
        print(max_count)
        result = [key for key, value in self.count.items() if value == max_count]
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(4)


answer = Solution()
print(answer.findMode(root))        
