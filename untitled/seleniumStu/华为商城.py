# author:JinMing time:2020-04-04
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome('F:\\Tool\selenium\chromedriver.exe')
# driver.implicitly_wait(10)
# driver.get('https://www.vmall.com/')
# #获得商品所有标签
# Alltitle=driver.find_elements_by_css_selector('.b .category-list li[id]')
# for i in Alltitle:
#     ActionChains(driver).move_to_element(i).perform()
#     #找到一级菜单
#     print("一级菜单:",i.find_element_by_xpath('./div[1]//a').text)
#     #找到二级菜单
#     twotitle=i.find_elements_by_xpath('./div[2]//span')
#     for f in twotitle:
#         print('\t',f.text)
#
# #浏览器向下拖动
# driver.execute_script('window.scrollBy(0,900)')
# print("=" * 10, "分割符", "=" * 10)
#
# #找到每一个单品
# liSlin=driver.find_elements_by_xpath('//div[@class=\'span-968 fl\']/ul/li')
# for i in liSlin:
#     if not(i.find_elements_by_xpath('./a//span')and '爆款'in i.find_element_by_xpath('./a//span')[0].text):
#         continue
#     #取爆款商品名称
#     hotName=i.find_element_by_xpath('//div[@class=\'span-968 fl\']/ul/li//a//div').text
#     #获取商品价格
#     hotprice=i.find_element_by_xpath('//div[@class=\'span-968 fl\']/ul/li//a//p[@class=\'grid-price\']').text
#     print(f'爆款商品:{hotName},价格:{hotprice}')
#
# driver.quit()



print('name is \n tom')

print(str(23)+'hello')
print('kkk','hello')
print('hello\n'*3)
print('='*3+'分隔符'+'='*3)

str1='hujijjnkkk'

print(str1[::-1])







