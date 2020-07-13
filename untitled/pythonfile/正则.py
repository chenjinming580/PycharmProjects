# author:JinMing time:2020-04-21
import xlwt
import requests,re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 1- 新建一个excel文件
workBook = xlwt.Workbook(encoding='uft-8')#缓存里
#2- 创建一个子表
workSheet = workBook.add_sheet('51job',True)
colName = ['岗位名称','公司名称','地址','薪资','发布时间']
#3- 写进去
for one in range(0,len(colName)):# 0 1 2 3 4
   #写单元格
   workSheet.write(0,one,colName[one])#(行编号，列编号，内容)

def get_pagenum():
    web_url=f'https://search.51job.com/list/150200,000000,2720,01,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
    resp=requests.get(web_url, verify=False, headers=header)
    resp.encoding = 'gbk'
    pages=int(re.findall('<span class="td">共(.*?)页，到第</span>',resp.text,re.S)[0])
    return pages

row=1
for one in range(1,get_pagenum()+1):
    web_url = f'https://search.51job.com/list/150200,000000,2720,01,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,{one}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
    resp = requests.get(web_url,verify=False,headers=header)
    resp.encoding = 'gbk'

    # 1- 想查看发出去的请求头 或者 请求体：fiddler抓包，
    # print(resp.request.headers)#请求头
    # print(resp.request.body)#请求体s
    # ----------------------2、解析响应数据------------------
    # print(resp.text)
    # ----------------------3、提取有效数据------------------
    info = re.findall('<div class="el">(.*?)</div>', resp.text, re.S)

    for line in info:
        temp=re.findall('<a target="_blank" title="(.*?)" href',line,re.S)
        jobname=temp[0].strip()
        workSheet.write(row,0,jobname)
        company=temp[1].strip()
        workSheet.write(row,1,company)
        address = re.findall('<span class="t3">(.*?)</span>', line, re.S)[0]
        workSheet.write(row,2,address)
        salary = re.findall('<span class="t4">(.*?)</span>', line, re.S)[0]
        workSheet.write(row,3,salary)
        jobTime = re.findall('<span class="t5">(.*?)</span>', line, re.S)[0]
        workSheet.write(row,4,jobTime)
        row +=1



workBook.save('F:\\res_51job.xls')



















































