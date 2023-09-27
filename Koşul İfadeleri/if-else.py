# If & Else koşul ifadeleri, sorgulanan ifadenin istediğimiz veya istemediğimiz duruma göre izleyeceği yolu belirler.

username = "zenith"
password = "1234"


# if (username == "zenith") and (password == "1234"):
#   print("merhaba")
# else:
# print("username ya da parola yanlıştır")

if username == "zenith":
    if password == "12345":
        print("merhaba")
    else:
        print("parola yanlış")
else:
    print("username yanlış")
