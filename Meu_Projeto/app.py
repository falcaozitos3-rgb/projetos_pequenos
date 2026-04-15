from flask import Flask, render_template, request #importação do flask e do render template para renderizar os arquivos html
app = Flask(__name__) #criação da aplicação flask, passando o nome do módulo atual como argumento.
@app.route("/", methods=["GET","POST"])# definição da rota para a função 'index', que será executada quando a rota '/' for acessada.
# O método 'GET' indica que essa rota aceitará requisições do tipo GET.
def sistema_acesso(): #definição da função 'index', que será executada quando a rota '/' for acessada.
    mensagem = "" #variável 'mensagem' recebe a string "sistema de acesso"
    #'Render_template'  vai procurar o arquivo 'index.html' dentro da pasta 'templates' e renderizá-lo como resposta
    #para a rota '/'
    if request.method == "POST": #verifica se o método da requisição é POST
        

#Entrada
        nome = request.form.get("nome") #nome do usuario
        idade = int(request.form.get("idade"))#idade do usuario
        cadrastro = request.form.get("cadastro") #cadastro do usuario

# saida
        idade_input = request.form.get("idade") 
        if idade_input:
            idade = int(idade_input) #converte a entrada de idade para um número inteiro
                #maior de idade e tem cadastro
            if idade >= 18 and cadrastro == "sim":
                mensagem = f"acesso permitido, tem cadrastro, e é maior de idade: {nome}!"
                #menor de idade, mas tem cadastro
            elif idade < 18 and cadrastro == "sim":
                mensagem = f" você é menor de idade, mas tem cadastro: {nome}!\n poderá entrar, mas com acompanhante apenas. "
                #menor de idade e não tem cadastro
            elif idade < 18 and cadrastro == "não":
                mensagem = f"acesso negado, não tem cadastro e é menor de idade: {nome}!"
                #maior de idade, mas não tem cadastro
            elif idade >= 18 and cadrastro == "não":
                mensagem = "acesso permitido tem mais de 18 anos, no entanto não \n tem o cadrastro, faça o cadrastro ao entrar."

      


    return render_template('index.html', resposta=mensagem) #renderiza o arquivo 'index.html' e passa a variável 'mensagem' para o
                                                            # template, permitindo que ela seja usada dentro do arquivo HTML.

if __name__ == "__main__":
    app.run(debug=True)



