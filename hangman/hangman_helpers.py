import pygame
import random

def setup_game(window_width=1000, window_height=400):
    """
    Initialize the game window and basic elements.

    Arguments (needed): None
    Arguments (optional): window_width
                          window_height
    Returns: Game window/screen
    """
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Hangman")
    return window

def load_images():
    """
    This function loads all of the images needed for hangman.
    It allows the program to access the pictures in the folder and
    stores the names so that the program can find them later.

    Arguments (needed): None
    Arguments (optional): None
    Returns: A list of all image addresses needed.
    """
    images = []
    for i in range(1, 8):
        image = pygame.image.load(f"man{i}.png")
        images.append(image)
    return images

def pick_word(word_list=None):
    """
    Picks a random word from the list provided.

    Arguments (needed): word_list
    Arguments (optional): None
    Returns: A random word picked from the provided list of words.
    """
    if word_list is None:
        word_list = ["python", "game", "code", "fun", "learn"]
    return random.choice(word_list).lower()

def create_text(text, size=20, color='black'):
    """
    Creates a text surface.
    (These surfaces are then put onto the screen in another function.)

    Arguments (needed): text
    Arguments (optional): size, color
    Returns: A text surface containing the text and optional specifications
             given.
    """
    font = pygame.font.SysFont("comicsans", size)
    return font.render(text, True, color)

def draw_game(window, title, images, mistakes, word, guessed_letters,
              score=None, score_location=None, screen_keyboard=False, width=1000):
    """
    This function draws everything provided to the function onto the screen.

    Arguments (needed): window, title, images, mistakes, word, guessed_letters
    Arguments (optional): score (text surface with score text)
                          score_location (location)
                          screen_keyboard (on screen keyboard toggle)
                          width (width of the game window)
    Returns: Nothing
    """
    window.fill('white')

    # Draw title
    title_surface = create_text(title, 10)
    window.blit(title_surface, (width/2 - title_surface.get_width()/2, 10))

    # Draw word with blanks
    display_word = ""
    for letter in word:
        display_word += letter + " " if letter in guessed_letters else "_ "
    word_text = create_text(display_word)
    window.blit(word_text, (500, 250))

    # Draw hangman image
    window.blit(images[mistakes], (50, 50))

    # Score
    if score is not None and score_location is not None:
        window.blit(score, score_location)

    # On-Screen Keyboard
    if screen_keyboard:
        draw_keyboard(window, guessed_letters)

    pygame.display.update()


def check_win(word, guessed_letters):
    """
    This function checks if the player has guessed all letters needed.

    Arguments (needed): word (final word),
                        guessed_letters (collection of guessed letters)
    Arguments (optional): None
    Returns: True or False depending on if the game was won.
    """
    return all(letter in guessed_letters for letter in word)

def show_result(window, message, color, width=1000, height=400):
    """
    Show win/lose message.

    Arguments (needed): window (where should the text go),
                        message (win/lose message),
                        color (color of text)
    Arguments (optional): width (width of the game window)
                          height (height of the game window)
    Returns: Nothing
    """
    window.fill('white')
    text = create_text(message, 40, color)
    window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw_keyboard(window, guessed, width=1000):
    """
    Displays all the letters in the alphabet onto the screen.

    Arguments (needed): window (where should the text go),
                        guessed (guessed letters)
    Arguments (optional): width (width of the game window)
    Returns: Nothing
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    start_x = 1000 // 28
    start_y = 320

    for i, letter in enumerate(letters):
        x = start_x + (i * start_x) # shift to the right
        y = start_y
        color = 'gray' if letter in guessed else 'black'
        text = create_text(letter, 30, color)
        window.blit(text, (x, y))
