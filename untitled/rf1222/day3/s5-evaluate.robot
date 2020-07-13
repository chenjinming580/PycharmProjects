#evalueate

*** Test Cases ***
case1
    ${list}   evaluate   [i for i in range(100)]
    ${list}   evaluate  $list[:30]
    ${dict}    evaluate  {"a":'hello',"b":3}
    ${var1}    evaluate  $dict.update({"a":"world"})
    #eval函数不能执行赋值操作  $dict["a"]=123  执行不了
    log to console  ${var1}
    log to console  ${dict}
    log to console  ${list}