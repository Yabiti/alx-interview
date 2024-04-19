#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich
#Adieu, adieu, to Liesl, Friedrich, and Louisa
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
import inflect
p = inflect.engine()
text = ["Adieu", "adieu"]
while True:
    try:
        name = input("name: ")
    except EOFError:
        print()
        break
    text.append(name)
new_text = p.join(text)
print(new_text)