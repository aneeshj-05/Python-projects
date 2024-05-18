import time

def print_with_delay(text, delay=0.05):
    """Print text with a delay for each character to simulate typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def welcome_message():
    """Display a welcome message."""
    messages = [
        "Welcome to the Horror Mad Libs game!",
        "You'll be asked to provide different types of words.",
        "Let's create a spooky story together!\n"
    ]
    for message in messages:
        print_with_delay(message, 0.05)

def get_user_inputs(word_types):
    """Prompt the user for a list of words based on word types."""
    return [input(f"Please enter a {word_type}: ") for word_type in word_types]

def display_story(story):
    """Display the final story."""
    print("\nHere is your completed Horror Mad Libs story:\n")
    print_with_delay(story, 0.05)

def main():
    welcome_message()
    
    # List of word types needed for the horror story
    word_types = [
        "adjective", "adjective", "noun", "place", "adjective", 
        "noun", "animal", "adjective", "verb", 
        "noun", "adjective", "adjective", "body part", 
        "adjective", "adjective", "adjective", "noun", "verb ending in 'ing'", "noun"
    ]
    
    # Collecting user inputs
    user_inputs = get_user_inputs(word_types)
    
    # Horror story template
    story_template = (
        "It was a {0}, {1} night. The {2} was full as I walked through the dark, abandoned {3}. "
        "The air was {4} and the sound of {5} echoed in the distance. Suddenly, a {6}, {7} creature appeared and started to {8} towards me. "
        "I stumbled over a {9} and felt a {10} shiver run down my spine. The {11}, {12} eyes of the creature stared right at me. "
        "With a trembling {13}, I reached for my {14} phone, but it was no use. The battery was dead. "
        "I needed to find a way out, but the {15} fog made it impossible to see. Just as I thought it was the end, I remembered the {16} I had in my pocket. "
        "I quickly pulled it out and started {17}, hoping to scare away the creature. To my surprise, the {18} vanished into thin air."
    )
    
    # Formatting the story with user inputs
    story = story_template.format(*user_inputs)
    
    display_story(story)

if __name__ == "__main__":
    main()

