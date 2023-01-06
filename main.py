import pyautogui
import speech_recognition as sr

r = sr.Recognizer()

def listen_for_command():
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio, language='th-TH') //add thai language
    print(f"You said: {command}")
    return command
  except sr.UnknownValueError:
    print("ขออภัย, ฉันไม่เข้าใจสิ่งที่คุณพูด")
    return None
  except sr.RequestError:
    print("ขออภัย, ฉันมีปัญหาในการเชื่อมต่ออินเทอร์เน็ต")
    return None

while True:
  command = listen_for_command()
  if command == "เลื่อนเมาส์ขึ้น":
    pyautogui.moveRel(0, -10)
  elif command == "เลื่อนเมาส์ลง":
    pyautogui.moveRel(0, 10)
  elif command == "เลื่อนเมาส์ไปทางซ้าย":
    pyautogui.moveRel(-10, 0)
  elif command == "เลื่อนเมาส์ไปทางขวา":
    pyautogui.moveRel(10, 0)
  elif command == "คลิกซ้าย":
    pyautogui.click()
  elif command == "คลิกขวา":
    pyautogui.rightClick()
  elif command == "เลื่อนขึ้น":
    pyautogui.scroll(10)
  elif command == "เลื่อนลง":
    pyautogui.scroll(-10)   
  elif command == "ปิดการทำงาน":
    break
