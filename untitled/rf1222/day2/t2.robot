#引入自定义的库文件
*** Settings ***
Library  222
#Library  pylib.mylib3

#导入自定义库，执行的时候需要指定pythonpath
# robot -P . Template.robot 指在同一个目录下
*** Test Cases ***
case1
    ${var}  gettime2
    log to console  ${var}

#case2
#    ${var}   webapi   http://www.baidu.com
#    log to console  ${var}


