import subprocess
import os
import glob
import time
import win32com.client
import win32gui
import win32process

# ===== App mapping =====
APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "control panel": "control.exe",
}

shell = win32com.client.Dispatch("Shell.Application")

# ===== Focus CMD =====
def focus_cmd_window():
    pid = os.getpid()

    def enum_handler(hwnd, _):
        try:
            _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
            if window_pid == pid and win32gui.IsWindowVisible(hwnd):
                win32gui.SetForegroundWindow(hwnd)
        except:
            pass

    win32gui.EnumWindows(enum_handler, None)

# ===== Functions =====
def open_app(app):
    if app in APPS:
        subprocess.Popen(APPS[app])
        time.sleep(0.1)
        focus_cmd_window()
        print(f"Opened {app}")
    else:
        print("App not found")

def find_file(filename):
    paths = glob.glob(rf"C:\Users\atiwitwi\**\{filename}", recursive=True)
    if paths:
        print("Found:")
        for p in paths:
            print(p)
    else:
        print("File not found")

def open_folder(path_or_name, root=r"C:\Users\atiwitwi"):
    # ถ้าเป็น path เต็ม
    if os.path.exists(path_or_name):
        shell.Open(path_or_name)
        time.sleep(0.1)
        focus_cmd_window()
        print(f"Opened folder: {path_or_name}")
        return

    # ถ้าเป็นชื่อโฟลเดอร์
    name = path_or_name.lower()
    for current_root, dirs, _ in os.walk(root):
        for d in dirs:
            if d.lower() == name:
                path = os.path.join(current_root, d)
                shell.Open(path)
                time.sleep(0.1)
                focus_cmd_window()
                print(f"Opened folder: {path}")
                return

    print("Folder not found")

def close_folder_by_name(folder_name):
    folder_name = folder_name.lower()
    found = False

    for window in shell.Windows():
        try:
            path = window.Document.Folder.Self.Path
            last = os.path.basename(path).lower()
            if last == folder_name:
                window.Quit()
                print(f"Closed folder: {path}")
                found = True
        except:
            pass

    if not found:
        print("Folder window not found")

# ===== Main loop =====
print("Python Bot (pywin32 version)")
print("Type 'exit' or 'q' to quit")

while True:
    command = input("Command: ").lower().strip()

    if command in ("exit", "q"):
        print("Bye")
        break

    elif command.startswith("open folder "):
        value = command.replace("open folder ", "").strip()
        open_folder(value)

    elif command.startswith("close folder "):
        folder_name = command.replace("close folder ", "").strip()
        close_folder_by_name(folder_name)

    elif command.startswith("find file "):
        filename = command.replace("find file ", "").strip()
        find_file(filename)

    elif command.startswith("open "):
        app = command.replace("open ", "").strip()
        open_app(app)

    else:
        print("Unknown command")
