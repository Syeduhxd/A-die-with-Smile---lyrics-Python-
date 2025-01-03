import time
from colorama import init, Style
import sys

init(autoreset=True)

def slow_print(text, delay=0.1, style=Style.BRIGHT):
    try:
        for char in text:
            sys.stdout.write(style + char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")  
        sys.stdout.flush()
    except Exception as e:
        print(f"Error during printing: {e}")

def display_lyrics():
    lyrics = [
        ("- So I'ma love you every night like it's the last night 🌙", 0.05, Style.BRIGHT),
        ("- like it's the last night 💫", 0.07, Style.BRIGHT),
        ("- If the world was ending 💥", 0.1, Style.BRIGHT),
        ("- I'd wanna be next to you 😘", 0.15, Style.BRIGHT),
        ("- If the party was over 🎉", 0.07, Style.BRIGHT),
        ("- and our time on Earth was through ⏳", 0.15, Style.BRIGHT),
        ("- I'd wanna hold you just for a while 💑", 0.12, Style.BRIGHT),
        ("- and die with a smile 😊", 0.15, Style.BRIGHT),
        ("- If the world was ending 🌍", 0.12, Style.BRIGHT),
        ("- I'd wanna be next to you 💕", 0.12, Style.BRIGHT),
    ]

    for line in lyrics:
        text = line[0]
        char_delay = line[1]
        style = line[2]

        slow_print(text, delay=char_delay, style=style)
        
        if text == "- I'd wanna be next to you 😘":
            time.sleep(2) 
        if text == "- And our time on Earth was through ⏳🌎":
            time.sleep(2) 

        time.sleep(0.3)
def main():
    slow_print("💕 This is for you 💕", delay=0.05, style=Style.BRIGHT)
    display_lyrics()

if __name__ == "__main__":
    main()