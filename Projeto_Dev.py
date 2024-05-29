# PASSO A PASSO PARA CRIAÇÃO DE UM SITE/SISTEMA COM CHAT AO VIVO:

    # Instalação das bibliotecas necessárias:
        # Flet-> pip install flet        
    # Título -> "DuZap"
    # Botão -> "Iniciar Chat"
        # Abre uma popup
            # Título -> "Seja bem vindo(a) ao DuZap!"
            # Caixa de mensagem/Conteúdo -> "Escreva seu nome"
            # Botão -> "Entrar no chat"
                # Fecha a popup
                # Título "Duzap" desaparece
                # Botão "Iniciar Chat" desaparece
                # Chat abre
                # "{Nome da pessoa} + {entrou no chat}" aparece
                # Caixa de mensagem -> "Digite sua mensagem" + Botão -> "Enviar" aparece
                # Após enviar uma mensagem -> "{Nome da pessoa}: + {mensagem}" aparece


# Importação das bibliotecas necessárias:
import flet as ft

# Criar a função principal do seu aplicativo:
def main(pagina):
    # Criar todas as funcionalidades:
        # Criar os elementos:  

    titulo = ft.Text("DuZap!")
    titulo_popup = ft.Text("Seja bem vindo(a) ao DuZap!")
    campo_nome_usuario = ft.TextField(label="Escreve seu nome")

    chat = ft.Column()

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}:{texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()
      
    campo_mensagem = ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem,botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        popup.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        title=titulo_popup,
        content=campo_nome_usuario,
        actions=[botao_entrar])
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True  
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

        # Adicionar os elementos na página:
    pagina.add(titulo)
    pagina.add(botao_iniciar)

        # Criar o canal/túnel de comunicação (permite a troca de informações entre usuários):
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    

# Executar o seu aplicativo:
ft.app(main, view= ft.WEB_BROWSER)
