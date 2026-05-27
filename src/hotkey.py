from AppKit import NSEvent, NSKeyDownMask
import threading


class HotkeyListener:
    def __init__(self, callback):
        self.callback = callback
        self._thread = None

    def _listen(self):
        def handler(event):
            flags = event.modifierFlags()
            char = event.charactersIgnoringModifiers()
            has_cmd  = bool(flags & 0x8)   # cmd
            has_option = bool(flags & 0x80000)   # option
            char  = event.charactersIgnoringModifiers()
            if has_cmd and has_option and char and char.lower() == 'j':
                self.callback()

        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(
            NSKeyDownMask, handler
        )
        from AppKit import NSRunLoop, NSDate
        while True:
            NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.1)
            )

    def start(self):
        self._thread = threading.Thread(target=self._listen, daemon=True)
        self._thread.start()

    def stop(self):
        pass