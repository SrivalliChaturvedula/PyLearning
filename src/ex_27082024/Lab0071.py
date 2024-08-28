def start():
    print("Before running the UI TC")
    print("Start the browser")


def end():
    print("After running the UI TC")
    print("Quitting the browser")


def test_ui():
    start()
    print("Testing UI of the application")
    end()


test_ui()
