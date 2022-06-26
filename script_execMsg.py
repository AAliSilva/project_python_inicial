msg = enviarMensagens("Message")
enviar_email(msg, "A Test User <alice.alves@aluno.faculdadeimpacta.com.br>", "alice.alves@aluno.faculdadeimpacta.com.br>", "Test send email")

realizar_ping('minhacasa.edu.br')
realizar_ping('www.google.com')
realizar_ping('186.202.153.153')

verificar_portas("www.google.com")
verificar_portas("186.202.153.153")
verificar_portas("www.minhacasa.edu.br")

verificar_servidor('www.google.com.br', 80)
verificar_servidor('186.202.153.153', 80)
verificar_servidor('www.minhacasa.edu.br', 80)
