import time
import threading

class Incrementer:
    def __init__(self):
        self.value = 0
        self.running = True
        self.thread = threading.Thread(target=self.increment_loop)
        self.thread.start()

    def increment_loop(self):
        while self.running:
            time.sleep(10)  # Aguarda 10 segundos
            self.value += 25
            #print(f"Valor atualizado: {self.value}")

    def stop(self):
        self.running = False
        self.thread.join()

#
# inc = Incrementer()
# try:
#     while True:
#         time.sleep(1)  # Mantém o programa rodando
# except KeyboardInterrupt:
#     inc.stop()  # Para a thread ao interromper o programa
