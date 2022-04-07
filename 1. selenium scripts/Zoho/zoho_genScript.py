import os
#note: Zoho does not allow symbols and digits only. 
#can observe that with digits no symbols, it is deterministic, always starts with digit. 
#8 characters
print("Starting letters only, 8 characters")
os.system("python3 zoho_generator.py -o zoho-letter-8.txt -n 10000 -l 8 -d 'false' -s 'false'")
print("Starting letters and digits, 8 characters")
os.system("python3 zoho_generator.py -o zoho-letterdigit-8.txt -n 10000 -l 8 -d 'true' -s 'false'")
print("Starting letters and symbols, 8 characters")
os.system("python3 zoho_generator.py -o zoho-lettersymbol-8.txt -n 10000 -l 8 -d 'false' -s 'true'")
print("Starting all, 8 characters")
os.system("python3 zoho_generator.py -o zoho-all-8.txt -n 10000 -l 8 -d 'true' -s 'true'")


#12 characters

print("Starting letters only, 12 characters")
os.system("python3 zoho_generator.py -o zoho-letter-12.txt -n 10000 -l 12 -d 'false' -s 'false'")
print("Starting letters and digits, 12 characters")
os.system("python3 zoho_generator.py -o zoho-letterdigit-12.txt -n 10000 -l 12 -d 'true' -s 'false'")
print("Starting letters and symbols, 12 characters")
os.system("python3 zoho_generator.py -o zoho-lettersymbol-12.txt -n 10000 -l 12 -d 'false' -s 'true'")
print("Starting all, 12 characters")
os.system("python3 zoho_generator.py -o zoho-all-12.txt -n 10000 -l 12 -d 'true' -s 'true'")

#20 characters
print("Starting letters only, 20 characters")
os.system("python3 zoho_generator.py -o zoho-letter-20.txt -n 10000 -l 20 -d 'false' -s 'false'")
print("Starting letters and digits, 20 characters")
os.system("python3 zoho_generator.py -o zoho-letterdigit-20.txt -n 10000 -l 20 -d 'true' -s 'false'")
print("Starting letters and symbols, 20 characters")
os.system("python3 zoho_generator.py -o zoho-lettersymbol-20.txt -n 10000 -l 20 -d 'false' -s 'true'")
print("Starting all, 20 characters")
os.system("python3 zoho_generator.py -o zoho-all-20.txt -n 10000 -l 20 -d 'true' -s 'true'")