import pyautogui
import speech_recognition as sr

r = sr.Recognizer()

def listen_for_command():
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio)
    print(f"You said: {command}")
    return command
  except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")
    return None
  except sr.RequestError:
    print("Sorry, I am having trouble connecting to the internet.")
    return None

while True:
  command = listen_for_command()
  if command == "move mouse up":
    pyautogui.moveRel(0, -10)
  elif command == "move mouse down":
    pyautogui.moveRel(0, 10)
  elif command == "move mouse left":
    pyautogui.moveRel(-10, 0)
  elif command == "move mouse right":
    pyautogui.moveRel(10, 0)
  elif command == "quit":
    break
