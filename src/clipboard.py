import subprocess
import time
import pyperclip

def get_selected_text():
    #현재 클립보드 백업
    backup = pyperclip.paste()

    #Cmd+C로 선택된 텍스트 복사
    subprocess.run(['osascript', '-e',
                    'tell application "System Events" to keystroke "c" using command down'])
    time.sleep(0.3)

    selected = pyperclip.paste()

    #선택된 텍스트가 없거나 백업이랑 같으면 None 반환
    if not selected or selected == backup:
        return None, backup
    
    return selected, backup


def replace_selected_text(converted_text, original_clipboard):
    #변환된 텍스트 클립보드에 넣고 붙혀넣기
    pyperclip.copy(converted_text)
    time.sleep(0.05)

    subprocess.run(['osascript', '-e',
                    'tell application "System Events" to keystroke "v" using command down'])
    time.sleep(0.1)

    #원래 클립보드 복원
    pyperclip.copy(original_clipboard)