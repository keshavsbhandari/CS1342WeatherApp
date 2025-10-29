import subprocess

def send_imessage(phone_number, message):
    """
    Sends an iMessage through the Messages app on macOS.

    Parameters:
    phone_number (str): The recipient's phone number or email (use full number with country code).
    message (str): The message you want to send.
    """
    # AppleScript command to send the message
    script = f'''
    imessage -t "{message}" -c "{phone_number}"
    '''
    # Execute the AppleScript command
    process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Error: {stderr.decode()}")

# Example usage
send_imessage("0000000000", "Absolutely! Texans are known for their warmth, resilience, and a fierce pride in their home state. From the wide-open landscapes to the bustling cities, there's a sense of camaraderie and independence that defines Texas. Texans embrace the pioneering spirit with a tenacity that seems to grow with every generation, facing challenges with a grit that’s as big as the state itself.")  # Replace with the recipient's phone number or email