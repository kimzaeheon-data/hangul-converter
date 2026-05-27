import rumps
import threading
from src.converter import hangul_to_qwerty
from src.clipboard import get_selected_text, replace_selected_text
from src.hotkey import HotkeyListener


class HangulConverterApp(rumps.App):
    def __init__(self):
        super().__init__("한→A", quit_button="종료")
        self.menu = ["변환하기 (Ctrl+Shift+H)", None]
        self.hotkey_listener = HotkeyListener(callback=self.convert)
        self.hotkey_listener.start()

    def convert(self):
        selected, backup = get_selected_text()

        if not selected:
            rumps.notification("한글 변환기", "", "변환할 텍스트를 선택해주세요.")
            return

        converted = hangul_to_qwerty(selected)
        replace_selected_text(converted, backup)
        rumps.notification("한글 변환기 ✅", "", f"{selected} → {converted}")

    @rumps.clicked("변환하기 (Ctrl+Shift+H)")
    def on_click_convert(self, _):
        threading.Thread(target=self.convert, daemon=True).start()