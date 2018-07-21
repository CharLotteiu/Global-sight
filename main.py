# -*- coding: utf-8 -*-
"""

"""

import iSearch, iTranslate

if __name__ == '__main__':   
    searchtool = iSearch.iSearch()
    translatetool = iTranslate.iTranslate()
    with open('LocaleResource_en_US.properties') as file: # 打开测试文件，默认模式为‘r’，只读模式
        lines = file.readlines()
        file.close()# 读取文件全部内容
        with open ('LocaleResource_zh_CN.properties',"a") as f:
            f.seek(0)      
            f.truncate()   #清空文件
            for line in lines: # 遍历所有行
                if(line == '\n'):
                    f.write(line)
                    continue
                else:
                    diction = searchtool.imatch(line)
                    flag = diction['flag']
                    pattern = diction['pattern']
                    if (flag == 0 and pattern == 3):
                        content = diction['result']
                        head = diction['head']
                        middle = diction['middle']
                        translation = translatetool.itranslate(content)
                        fline = head + middle + translation + '\n'
                    else:
                        fline =line
                    print('第 ' + str(translatetool.record) + ' 次调用\n')
                    f.write(fline)
        f.close()
                
            
