import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install requests")
    os.system("pip install click")
    os.system("pip install fake_headers")
    os.system("pip install colorama")
    os.system("pip install fade")
elif c == "1":
    os.system("pip3 install requests")
    os.system("pip3 install click")
    os.system("pip3 install fake_headers")
    os.system("pip3 install colorama")
    os.system("pip3 install fade")
   
print("Done.")
