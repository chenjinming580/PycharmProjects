*** Test Cases ***
case1
    #如何使用变量和定义时候使用的符号没有关系，只和传参的时候有关
    ${list}   create list  1  2   3
    log to console  ${list}[0]  #以list形式传参，相当于展开列表内的元素，作为多个参数进行传参
    log to console  ${list[0]}   #以普通形式传参，就把变量作为一个整体进行传递
    log many  @{list}
case2
    #操作字典
    &{dict}   create dictionary   a=1323123123   b=2    c=3
#    log to console  ${dict}
#    log many  &{dict}  #传递的字典的键值对
    log to console  ${dict}[a]
    log to console  ${dict['a']}


