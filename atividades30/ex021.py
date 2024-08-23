import pygame

pygame.mixer.init()

pygame.mixer.music.load('C:\\Users\\ACER\\Desktop\\teste.mp3')

pygame.mixer.music.play()

# Verificar se o áudio está sendo reproduzido
if pygame.mixer.music.get_busy():
    print("Áudio está tocando.")
else:
    print("Falha ao reproduzir o áudio.")

# Manter o programa em execução enquanto o áudio está tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)