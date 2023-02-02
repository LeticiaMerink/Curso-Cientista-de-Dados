def cadastra_cliente (nome,email,cpf):
    cliente = {}
    cliente['nome'] = nome
    cliente['email'] = email
    cliente['cpf'] = cpf
    return cliente

def verifica_cadastro_ja_existente(cpf):
    cpf_clientes_cadastrados = [123,456,678,990,110]
    if cpf in cpf_clientes_cadastrados:
        print("Ops! Você já possui cadastro!")

def verifica_email_valido(email):
    if "@" not in email:
        print("Esse e-mail não é valido.")