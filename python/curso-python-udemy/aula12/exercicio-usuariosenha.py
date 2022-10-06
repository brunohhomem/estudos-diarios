usuario = input('Usuario: \n')
senha = input('Senha: \n')

usuario_bd = 'bruno'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
elif usuario_bd != usuario or senha_bd != senha:
    print('Usuario ou senha inválidos.')
