###python中文乱码问题的解决


1、在py文件开头写上这两行：

    #!/usr/bin/env python3
	# -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

2、申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须同时确保文本编辑器正在使用UTF-8 without BOM编码。

如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文。


###python字符串

ord：把字符转换为对应的ASCII或Unicode十进制表示
chr：把编码的十进制表示转换为对应的字符

- ord('A')  返回A的ASCII十进制表示
- ord('中') 返回“中”的Unicode十进制表示
- chr(65)   返回65的字符表示


encode:以Unicode表示的str通过encode()方法可以编码为指定的bytes，可以是ascii、gbk、utf-8等各种编码，例如：

'ABC'.encode('ascii')  # b'ABC'
'中文'.encode('utf-8')  # 

    print str * 2   # 输出字符串两次
    print str[0]# 输出字符串中的第一个字符
    print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
    print str[2:]   # 输出从第三个字符开始的字符串

    list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']
     
    print list   # 输出完整列表
    print list[0]# 输出列表的第一个元素
    print list[1:3]  # 输出第二个至第三个元素 
    print list[2:]   # 输出从第三个开始至列表末尾的所有元素
    print tinylist * 2   # 输出列表两次
    print list + tinylist# 打印组合的列表

python字符串连接的三种方法及其效率和适用场景

- 1.直接通过加号操作符连接
> 方法1，使用简单直接，但是网上不少人说这种方法效率低。
> 
> 之所以说python 中使用 + 进行字符串连接的操作效率低下，是因为python中字符串是不可变的类型，使用 + 连接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，当连续相加的字符串很多时(a+b+c+d+e+f+...) ，效率低下就是必然的了
> 
> 但是加号连接效率低是在连续进行多个字符串连接的时候出现的，如果连接的个数较少，加号连接效率反而比join连接效率高
		websit = 'python'+'tab'+'.com'

- 2.通过join方法：
> 方法2，使用略复杂，但对多个字符进行连接时效率高，只会有一次内存的申请。而且如果是对list的字符进行连接的时候，这种方法必须是首选

    	listStr = ['python','tab','.com']
    	website = ''.join(listStr)

- 3.通过替换
> 方法3：字符串格式化，这种方法非常常用，本人也推荐使用该方法



**list简单去重和倒序**

    s = [1,2,3,3]
    s = list(set(s))
    s = s[::-1]
> 如果之前定义了一个list变量，那么这时list函数将被list变量覆盖，`list(set(s))`会报`typeerror: 'list' object is not callable`错，只要使用`del list`删掉list变量即可

### python函数

