# -*- coding: utf-8 -*-
"""

"""
import re

class iSearch:
    def __init__(self):
        self.p1 = re.compile(r'#.*')
        self.p2 = re.compile(r'DO NOT TRANSLATE THIS SECTION')
        self.p3 = re.compile(r'([^=]*)(=\s*)(.*)') 
        self.p4 = re.compile(r'(\.htm)(.*)')
        self.flag = 0
        
    def isearch(self,content,num):
        n=num
        c=content
        result = None
        if(n==1):
            result = self.p1.search(c)
        elif(n==2):
            result = self.p2.search(c)
        elif(n==3):
            result = self.p3.search(c)
        elif(n==4):
            result = self.p4.search(c)
        return result

    def imatch(self, content):
        diction = {}
        result = None
        result_content=' '
        head = ''
        middle = ''
        c = content
        n = 0
        nums = [1,3]
        if(self.flag):
            pattern = 1
            result = self.isearch(c,1) 
            if (result != None):
                self.flag = 0

        else:
            while(result == None):
                result = self.isearch(c,nums[n])
                n+=1
                
            pattern = nums[n-1]
            
            if(pattern == 1):
                result1 = self.isearch(result.group(),2)
                if (result1 != None):
                    self.flag = 1
            elif(pattern == 3):
                result2 = self.isearch(result.group(3),4)
                if (result2 != None and result2.group(2) is ''):
                    pattern = 4
                else:
                    result_content = result.group(3)
                    head = result.group(1)
                    middle = result.group(2)
                
        diction['flag'] = self.flag
        diction['result'] = result_content
        diction['pattern'] = pattern
        diction['head'] = head
        diction['middle'] = middle
        
        return diction

