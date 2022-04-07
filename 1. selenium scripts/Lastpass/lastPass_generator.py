from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import argparse

def generate_lastPass(number_of_pw,length_of_pw,upper_case,lower_case,include_digits,include_special,output_file):
    #Initialize Driver
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('log-level=3')
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)

    #Set URL
    url = 'https://www.lastpass.com/features/password-generator'
    driver.get(url)

    #Define Manipulated Variables
    lowerCase = driver.find_element_by_xpath("//*[@id='lp-pg-uppercase']")
    upperCase = driver.find_element_by_xpath("//*[@id='lp-pg-lowercase']")
    incSpecial = driver.find_element_by_xpath("//*[@id='lp-pg-symbols']")
    incNumbers = driver.find_element_by_xpath("//*[@id='lp-pg-numbers']")
    passLength = driver.find_element_by_xpath("//*[@id='lp-pg-password-length']")
    
    
    #Set the Manipulated Variables
    desiredLength = length_of_pw
    desiredUpper = upper_case   
    desiredLower = lower_case
    desiredNumbers = include_digits
    desiredSpecial = include_special
    driver.execute_script("arguments[0].value='{}'".format(desiredLength),passLength)
    driver.execute_script("arguments[0].checked={}".format(desiredUpper),upperCase)
    driver.execute_script("arguments[0].checked={}".format(desiredLower),lowerCase)
    driver.execute_script("arguments[0].checked={}".format(desiredSpecial),incSpecial)
    driver.execute_script("arguments[0].checked={}".format(desiredNumbers),incNumbers)
    driver.execute_script("document.getElementsByClassName('lp-pg-generated-password__icon lp-pg-generated-password__icon-generate')[0].click();")

    #Initialize Password List
    passList = []

    for i in range(number_of_pw):
        generated_password =driver.find_element_by_xpath("//input[@id='GENERATED-PASSWORD']").get_attribute("value")
        passList.append("{}".format(generated_password))
        driver.execute_script("document.getElementsByClassName('lp-pg-generated-password__icon lp-pg-generated-password__icon-generate')[0].click();")
    
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
    parser.add_argument("-upper", help= "upper case, enter 'true' or 'false'",type = str, default = 'true')
    parser.add_argument("-lower", help= "lower case, enter 'true' or 'false'",type = str, default = 'true')
    parser.add_argument("-digit", help= "digits, enter 'true' or 'false'",type = str, default = 'false')
    parser.add_argument("-symbol", help= "special characters, enter 'true' or 'false'",type = str, default = 'false')
    args = parser.parse_args()

    generate_lastPass(output_file=args.o,number_of_pw=args.n,length_of_pw=args.l,upper_case=args.upper,lower_case=args.lower,include_digits=args.digit,include_special=args.symbol)