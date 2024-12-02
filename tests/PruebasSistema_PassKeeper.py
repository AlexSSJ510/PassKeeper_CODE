import pyautogui
import time

def test_app():
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.typewrite("python src/main.py\n")
    time.sleep(3)

    pyautogui.typewrite("user1\n")
    pyautogui.typewrite("app1\n")
    pyautogui.typewrite("P@ssw0rd1\n")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.screenshot("test_result.png")
    print("Revisar captura: test_result.png")

if __name__ == "__main__":
    test_app()
