import smtplib
class enviarMensagens:

    def __init__(self):
        message = MIMEText("TEST!")
        message["Subject"] = "Alert!"
        message["From"] = sender
        message["To"] = receiver
    def enviar_email(self, email, titulo):
        self.email = email
        self.titulo = titulo

        sender = "Private Person <alicyalves199@gmail.com>"
        receiver = "A Test User <alice.alves@aluno.faculdadeimpacta.com.br>"


        message = self.mensagem

        print(message)
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("e98bc320925dae", "eecc4df1afb91f")
            server.sendmail(sender, receiver, message.as_string())


        envio_email = enviarMensagens('Erro')
        envio_email.enviar_email("A Test User <alice.alves@aluno.faculdadeimpacta.com.br>", "titulo da mensagem")
