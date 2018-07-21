# -*- coding: utf-8 -*-
"""

"""
import machine_translation.youdaofanyi as youdao
import machine_translation.bingfanyi as bing

class iTranslate:
    def __init__(self):
        self.record = 0   
        self.btimes = 0 
        self.ydtimes = 0
    
    def itranslate(self, content):
        if(self.record>=2000):
            print('调用必应翻译')
            return self.bingtranslate(content)
        else:
            print("调用有道翻译")
            return self.youdaotranslate(content)
    
    def bingtranslate(self, content):
        translator = bing.BingFanyi("zh")
        translation = translator.translate(content) #翻译结果
        self.record += 1
        self.btimes += 1
        return translation
    
    def youdaotranslate(self, content):
        translator = youdao.YouDaoFanyi("zh")
        translation = translator.translate(content) #翻译结果
        self.record += 1
        self.ydtimes += 1
        return translation
        
    
