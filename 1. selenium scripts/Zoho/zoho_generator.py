from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import argparse

def generate_zoho(number_of_pw,length_of_pw,mixed_case,include_digits,include_special,output_file):
    #Initialize Driver
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('log-level=3')
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)

    #Set URL
    url = 'https://www.zoho.com/vault/password-generator/'
    driver.get(url)

    #Define Manipulated Variables
    mixedCase = driver.find_element_by_xpath("//*[@id='passGenMixedCase']")
    startAlpha = driver.find_element_by_xpath("//*[@id='startWithAlpha']")
    incSpecial = driver.find_element_by_xpath("//*[@id='specialChar']")
    incNumbers = driver.find_element_by_xpath("//*[@id='incNumbers']")
    passLength = driver.find_element_by_xpath("//*[@id='passrange']")

    #Set the Manipulated Variables
    desiredLength = length_of_pw   
    desiredCase = mixed_case
    desiredAlpha = 'false'
    desiredNumbers = include_digits
    desiredSpecial = include_special
    driver.execute_script("arguments[0].value='{}'".format(desiredLength),passLength)
    driver.execute_script("arguments[0].checked={}".format(desiredCase),mixedCase)
    driver.execute_script("arguments[0].checked={}".format(desiredAlpha),startAlpha)
    driver.execute_script("arguments[0].checked={}".format(desiredSpecial),incSpecial)
    driver.execute_script("arguments[0].checked={}".format(desiredNumbers),incNumbers)
    driver.execute_script("document.getElementsByClassName('zrefresh_btn')[0].click();")

    #Initialize Password List
    passList = []

    for i in range(number_of_pw):
        generated_password =driver.find_element_by_xpath("//input[@id='pass_gen']").get_attribute("value")
        passList.append("{}".format(generated_password))
        driver.execute_script("document.getElementsByClassName('zrefresh_btn')[0].click();")

    
    #Save into output file. Make this into an executable script with input selection.
    with open(output_file,'w') as f:
        for i in range(len(passList)):
            f.write("{}\n".format(passList[i]))
        f.close()

    driver.close()


if __name__ =="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-o",help = "Output File", required=True)
    parser.add_argument("-n",help = "Number of Passwords", type = int,default= 1000)
    parser.add_argument("-l",help = "length of password", type = int,default= 20)
    parser.add_argument("-m", help= "mix of upper and lower, enter 'true' or 'false'",type = str, default = 'true')
    parser.add_argument("-d", help= "to include digits, enter 'true' or 'false'",type = str, default = 'false')
    parser.add_argument("-s", help= "to include special characters, enter 'true' or 'false'",type = str, default = 'false')
    args = parser.parse_args()

    generate_zoho(output_file=args.o,number_of_pw=args.n,length_of_pw=args.l,mixed_case=args.m,include_digits=args.d,include_special=args.s)