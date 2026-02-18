#!/usr/bin/env python3
"""
Simple greeting program that responds to various greetings.
"""


def greet(message):
    """
    Respond to a greeting message.
    
    Args:
        message (str): The greeting message
        
    Returns:
        str: A response to the greeting
    """
    message = message.strip().upper()
    
    greetings = {
        "HI": "Hello! Welcome to the DT Fellowship Assignment repository!",
        "HELLO": "Hi there! How can I help you today?",
        "HEY": "Hey! Good to see you here!",
    }
    
    return greetings.get(message, "Hello! Nice to meet you!")


def main():
    """Main function to demonstrate the greeting functionality."""
    print(greet("HI"))
    print(greet("HELLO"))
    print(greet("HEY"))
    print(greet("Good morning"))


if __name__ == "__main__":
    main()
