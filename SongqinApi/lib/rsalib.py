# author:JinMing time:2020-04-30
import rsa

#1.待加密的字符串

def rsa1(str):
    (pubkey,privkey)=rsa.newkeys(1024)
    #3.用公钥加密
    pwd1=rsa.encrypt(str.encode(),pubkey)
    return {'pwd':pwd1,'pubkey':pubkey,'privkey':privkey}


dict=rsa1('123456')
print(dict['pubkey'])