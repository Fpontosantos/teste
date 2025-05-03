import re

def extrair_emails(texto):
    padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(padrao_email, texto)
    return ' '.join(emails) 

if __name__ == "__main__":
    texto = 'Favor enviar um e-mail para abc@hotmail.com com cópia para def@abc.com.br'
    resultado = extrair_emails(texto)
    print(resultado)