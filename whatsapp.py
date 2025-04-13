import pywhatkit as kit
from datetime import datetime

def schedule_whatsapp_message(phone_number, message, hour, minute):
    """
    Schedule a WhatsApp message to be sent at a specific time.
    
    Args:
        phone_number (str): Recipient's phone number in the format "+[country_code][number]".
        message (str): The message to send.
        hour (int): Hour (24-hour format) to send the message.
        minute (int): Minute to send the message.
    """
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message scheduled successfully for {hour}:{minute}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    print("Welcome to WhatsApp Scheduler!")
    phone_number = input("Enter the recipient's phone number (e.g., +1234567890): ")
    message = input("Enter the message you want to send: ")
    time_input = input("Enter the time to send the message (HH:MM in 24-hour format): ")
    
    try:
        hour, minute = map(int, time_input.split(":"))
        now = datetime.now()
        if hour < now.hour or (hour == now.hour and minute <= now.minute):
            print("Scheduled time must be in the future.")
        else:
            schedule_whatsapp_message(phone_number, message, hour, minute)
    except ValueError:
        print("Invalid time format. Please use HH:MM in 24-hour format.")