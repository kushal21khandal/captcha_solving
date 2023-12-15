
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import os
import time
# from tkinter import Tk
import tkinter as tk

driver = webdriver.Firefox()
# driver.maximize_window()

captcha_path = ('./sample/')
out_path = open('./output.txt', 'a')

driver.get('https://lens.google.com/search?p=AXAp4wiFv1OxSysgg5uQrOlLN2pORM-0wFCXFOUOM7SlVBhvR1aT_0U9KdD_Jw_r7L2GERXZ8M4P60BW2eZ0FE7HWOIF2eAWwJHq3ZvYaAJW5ZgqXPlJO34CmzK_gws3R13xcZfix1gEYTQ1EgkXOAvq-mZdmNsxbfXkeio_prE3kEe3H_umANiYLHd5JqX9ve5eND-EaHIRdEwJWQ61XaLZ6w6d5XzVwiXNazLxjiJGsWJ7twiGubzP&ep=gsbubb&hl=en-IN&re=df#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKRGxoWWpneE1EaGtMV1kyT0RRdE5ETmhaaTA1TlRoaExUQTFZbVJrTW1JMVl6a3hZaElmWnpsVFIyVmFNMDF2UkVGbFdVeHVaVFo2U1ROWFNFNUdTbVZDZDFaNFp3PT0iXQ==')

# driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb').click()

# upload_from_computer_button = driver.find_element(
#     By.CLASS_NAME, 'VfPpkd-StrnGf-rymPhb-b9t22c').click()

# subprocess.call("D:\\selenium_captcha_webreader_windows\\fileupload.exe")

for captcha in os.listdir(captcha_path):

    driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb').click()

    upload_from_computer_button = driver.find_element(
        By.CLASS_NAME, 'VfPpkd-StrnGf-rymPhb-b9t22c').click()

    # AutoIT or suprocess both have sleep options for the task
    subprocess.call(
        "D:\\selenium_captcha_webreader_windows\\without_loop_manual_file_upload.exe")

    # driver.find_element(
    #     By.ID, 'ucc-3').click()

    driver.find_element(
        By.XPATH, '/html/body/div[3]/c-wiz/div/c-wiz/div/div[1]/div/div[3]/div/div/span[2]/span').click()

    # driver.find_element(By.CLASS_NAME, 'VfPpkd-rOvkhd-jPmIDe-dgl2Hf').click()
    time.sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[3]/c-wiz/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div/div[2]').click()

    # driver.find_element(By.CLASS_NAME, 'VfPpkd-rOvkhd-jPmIDe-dgl2Hf').click()
    driver.find_element(
        By.XPATH, '/html/body/div[3]/c-wiz/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]').click()

    root = tk.Tk()
    spam = root.clipboard_get()
    out_path.write(spam)


driver.close()
