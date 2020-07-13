# author:JinMing time:2020-04-30
import rsa

#1.待加密的字符串
str="sdfsdfsdf"
#2.实例化加密对象
(pubkey,privkey)=rsa.newkeys(1024)
#3.用公钥加密
pwd1=rsa.encrypt(str.encode(),pubkey)
print("加密后的结果1为："+pwd1.hex())


pwd2=rsa.encrypt(str.encode(),pubkey)
print("加密后的结果2为："+pwd2.hex())

#4.用私钥解密
depwd1=rsa.decrypt(pwd1,privkey)
print("解密后的结果为："+depwd1.decode('UTF-8'))

depwd2=rsa.decrypt(pwd2,privkey)
print("解密后的结果为："+depwd2.decode('UTF-8'))