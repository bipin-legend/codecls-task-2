import time

def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    minutes = time_taken / 60
    wpm = num_words / minutes
    return wpm

def main():
    print("Welcome to the typing speed test!")
    print("Type the following text as fast as you can and press enter:")
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print(prompt_text)
    input("Press Enter when you are ready to start typing...")
    
    start_time = time.time()
    typed_text = input("Type the text: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    typing_speed = calculate_typing_speed(typed_text, time_taken)
    
    accuracy = sum(a == b for a, b in zip(prompt_text, typed_text)) / len(prompt_text) * 100
    
    print("\nTyping speed: {:.2f} WPM".format(typing_speed))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    main()
