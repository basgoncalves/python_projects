

def please_close_word():
    import pyautogui
    import time

    # Check if any Word documents are open
    while pyautogui.getWindowsWithTitle("Word"):
        # Ask the user to save and close all documents
        result = pyautogui.confirm(
            "Some Word documents are still open. Do you want to save and close them?",
            buttons=["Yes", "No", "Cancel"]
        )
        
        if result == "Yes":
            word_windows = pyautogui.getWindowsWithTitle("Word")
            # Press Alt+F4 to close all Word documents
            for window in word_windows:
                window.close()
                pyautogui.alert("All Word documents are closed.")
        elif result == "Cancel":
            return False
    # if function reaches this point, it means that all Word documents are closed
    return True

print(please_close_word())