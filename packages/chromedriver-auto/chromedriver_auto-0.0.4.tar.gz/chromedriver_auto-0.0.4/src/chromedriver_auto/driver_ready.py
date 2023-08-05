
import os
import platform
import subprocess
import zipfile
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service

def test():
    print('hiiiiiiiiii')
    return 'done'
# def get_operating_system():
#     return platform.system()

# # Example usage:
# os_name = get_operating_system()
# if os_name == "Windows":
#     file_path= str(os.getcwd()) + '/chrome/chromedriver-win'
# elif os_name == "Darwin":
#     file_path= str(os.getcwd()) + '/chrome/chromedriver-mac-arm64'
# try:
#     service = Service(executable_path=file_path)
#     driver = webdriver.Chrome(service=service)
# except:
#     file_path= os.getcwd()
#     print(file_path)
    
#     def get_chrome_version():
#         if platform.system() == 'Windows':
#             try:
#                 process = subprocess.Popen(['wmic', 'datafile', 'where', 'name="C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe"', 'get', 'Version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#                 output, error = process.communicate()
#                 if not error:
#                     version = output.decode().strip().split('\n')[1].strip()
#                     return version
#             except Exception as e:
#                 print("Error occurred:", e)
#         elif platform.system() == 'Darwin':  # macOS
#             try:
#                 process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 output, error = process.communicate()
#                 if not error:
#                     version = output.decode().strip().split(' ')[2]
#                     return version
#             except Exception as e:
#                 print("Error occurred:", e)
#         elif platform.system() == 'Linux':
#             try:
#                 process = subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 output, error = process.communicate()
#                 if not error:
#                     version = output.decode().strip().split(' ')[2]
#                     return version
#             except Exception as e:
#                 print("Error occurred:", e)

#         return None

#     chrome_version = get_chrome_version()
#     print(chrome_version)
#     def get_operating_system():
#         return platform.system()

#     # Example usage:
#     os_name = get_operating_system()
#     if os_name == "Windows":
#         def get_windows_architecture():
#             return platform.architecture()[0]
#         windows_arch = get_windows_architecture()

#         if windows_arch == '32bit':
#             download_url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chrome_version}/win32/chromedriver-win32.zip'
#         elif windows_arch == '64bit':
#             download_url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chrome_version}/win64/chromedriver-win64.zip'
#             print("Windows OS is 64-bit.")
        
#         r = requests.get(download_url, allow_redirects=True)
#         open('chromedriver-win.zip', 'wb').write(r.content)
        
#         with zipfile.ZipFile(f'{file_path}/chromedriver-win.zip', 'r') as zip:
#             try:
#                 zip.extractall(f'{file_path}/chrome/')
#             except:
#                 pass
#         try:
#             os.remove(f'{file_path}/chromedriver-win.zip')
#         except:
#             pass

#         file_path= str(os.getcwd()) + '/chrome/chromedriver-win'
#     elif os_name == "Darwin":
#         download_url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chrome_version}/mac-arm64/chromedriver-mac-arm64.zip'
#         r = requests.get(download_url, allow_redirects=True)

#         open('chromedriver-mac-arm64.zip', 'wb').write(r.content)

#         import zipfile
#         with zipfile.ZipFile(f'{file_path}/chromedriver-mac-arm64.zip', 'r') as zip:
#             try:
#                 zip.extractall(f'{file_path}/chrome/')
#             except:
#                 pass
#         try:
#             os.remove(f'{file_path}/chromedriver-mac-arm64.zip')
#         except:
#             pass


#         file_path= str(os.getcwd()) + '/chrome/chromedriver-mac-arm64'
#     service = Service(executable_path=file_path)
#     driver = webdriver.Chrome(service=service)
#     # return driver