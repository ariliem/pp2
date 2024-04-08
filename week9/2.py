import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Funk")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)

music_dir = '.'

def load_music():
    music_files = []
    for file in os.listdir(music_dir):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(music_dir, file))
    return music_files

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    play_music(music_files[current_song_index])

def play_previous():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    play_music(music_files[current_song_index])

music_files = load_music()

current_song_index = 0

running = True
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music(music_files[current_song_index])
                    playing = True
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()

    screen.fill(WHITE)

    status_text = "Playing" if playing else "Paused"
    text = font.render(status_text, True, BLACK)
    screen.blit(text, (50, 50))

    pygame.display.flip()

pygame.quit()
