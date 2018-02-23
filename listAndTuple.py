#声明一个list
classmates = ['Michael','Bob','Tracy']
print('list:',classmates)

#获取list长度
print('list长度:',len(classmates))

#输出list指定的项
print('第一项:',classmates[0],'----第二项:',classmates[1],'---第三项:',classmates[2])

#在list的末尾插入一个项
classmates.append('Adma')
print('在list的末尾插入一个项后：',classmates)
#输出list的末尾项
print('list末尾项:',classmates[-1])

#在索引1的位置插入一个值
classmates.insert(1,'Jack')
print('在索引1的位置插入一个值后：',classmates)

#删除list末尾项并返回删除的项
endItem = classmates.pop()
print('删除末尾项后:',classmates)
print('返回的删除项:',endItem)

#删除list指定位置项并返回删除项
endItem = classmates.pop(2)
print('删除索引2项:',classmates)
print('返回被删除的索引2项:',endItem);

#将索引1项的值替换为Sarah
classmates[1] = 'Sarah'
print('将索引1项的值替换为Sarah后:',classmates)