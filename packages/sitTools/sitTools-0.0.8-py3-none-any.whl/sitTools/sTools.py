# coding: utf-8
import requests, os, sys, tarfile, yaml, math, time
from Crypto.PublicKey import RSA

def gen_rsakey(path, host):
    '''
    Generate public and private RSA key for SSH auth use file at assigned path.
    在指定路徑中產生 SSH 認證用的 RSA 公鑰與私鑰檔案
    
    Argument:
    參數說明
    
    path = Assigned full path of key file.
           公鑰檔案的完整絕對路徑
           
    host = Hostname of login server.
           使用公鑰登入的伺服器主機名稱
    '''
    k_prv = RSA.generate(2048)
    k_pub = k_prv.public_key().export_key("OpenSSH")
    
    with open(path, 'wb') as key_file:
        k_host = bytes(f'{host} ', 'utf-8')
        key_file.write(k_host+k_pub)
        
    return None

