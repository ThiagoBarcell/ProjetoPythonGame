import threading

class Incrementador:
    def __init__(self):
        self.valor = 0
        self.executando = True

    def incrementar(self):
        while self.executando:
            self.valor += 5
            threading.Event().wait(10)  # Aguarda 10 segundos

    def iniciar(self):
        thread = threading.Thread(target=self.incrementar, daemon=True)
        thread.start()
        return thread

    def parar(self):
        self.executando = False

# Exemplo de uso
# incrementador = Incrementador()
# incrementador.iniciar()