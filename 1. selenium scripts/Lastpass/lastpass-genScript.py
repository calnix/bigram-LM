import os

#8 characters
print("Starting letters only, 8 characters")
os.system("python lastPass_generator.py -o lastpass-letter-8.txt -n 10000 -l 8 -upper 'true' -lower 'true' -digit 'false' -symbol 'false'")
print("Starting letter and digit, 8 characters")
os.system("python lastPass_generator.py -o lastpass-letterdigit-8.txt -n 10000 -l 8 -upper 'true' -lower 'true' -digit 'true' -symbol 'false'")
print("Starting letter and symbol, 8 characters")
os.system("python lastPass_generator.py -o lastpass-lettersymbol-8.txt -n 10000 -l 8 -upper 'true' -lower 'true' -digit 'false' -symbol 'true'")
print("Starting symbol and digit, 8 characters")
os.system("python lastPass_generator.py -o lastpass-symboldigit-8.txt -n 10000 -l 8 -upper 'false' -lower 'false' -digit 'true' -symbol 'true'")
print("Starting all characters, 8 characters")
os.system("python lastPass_generator.py -o lastpass-all-8.txt -n 10000 -l 8 -upper 'true' -lower 'true' -digit 'true' -symbol 'true'")
print("done with 8 chars")

#12 characters
print("Starting letters only, 12 characters")
os.system("python lastPass_generator.py -o lastpass-letter-12.txt -n 10000 -l 12 -upper 'true' -lower 'true' -digit 'false' -symbol 'false'")
print("Starting letter and digit, 12 characters")
os.system("python lastPass_generator.py -o lastpass-letterdigit-12.txt -n 10000 -l 12 -upper 'true' -lower 'true' -digit 'true' -symbol 'false'")
print("Starting letter and symbol, 12 characters")
os.system("python lastPass_generator.py -o lastpass-lettersymbol-12.txt -n 10000 -l 12 -upper 'true' -lower 'true' -digit 'false' -symbol 'true'")
print("Starting symbol and digit, 12 characters")
os.system("python lastPass_generator.py -o lastpass-symboldigit-12.txt -n 10000 -l 12 -upper 'false' -lower 'false' -digit 'true' -symbol 'true'")
print("Starting all characters, 12 characters")
os.system("python lastPass_generator.py -o lastpass-all-12.txt -n 10000 -l 12 -upper 'true' -lower 'true' -digit 'true' -symbol 'true'")
print("done with 12 chars")

#20 characters
print("Starting letters only, 20 characters")
os.system("python lastPass_generator.py -o lastpass-letter-20.txt -n 10000 -l 20 -upper 'true' -lower 'true' -digit 'false' -symbol 'false'")
print("Starting letter and digit, 20 characters")
os.system("python lastPass_generator.py -o lastpass-letterdigit-20.txt -n 10000 -l 20 -upper 'true' -lower 'true' -digit 'true' -symbol 'false'")
print("Starting letter and symbol, 20 characters")
os.system("python lastPass_generator.py -o lastpass-lettersymbol-20.txt -n 10000 -l 20 -upper 'true' -lower 'true' -digit 'false' -symbol 'true'")
print("Starting symbol and digit, 20 characters")
os.system("python lastPass_generator.py -o lastpass-symboldigit-20.txt -n 10000 -l 20 -upper 'false' -lower 'false' -digit 'true' -symbol 'true'")
print("Starting all characters, 20 characters")
os.system("python lastPass_generator.py -o lastpass-all-20.txt -n 10000 -l 20 -upper 'true' -lower 'true' -digit 'true' -symbol 'true'")
print("done with 20 chars")

