def before_and_after_testing_ui(custom_func_where_you_want_extra_functionality):
    # it has two parts wrap and call
    def wrapper():
        print("before testing UI TC")
        print("Start the browser")
        custom_func_where_you_want_extra_functionality()
        print("after testing UI TC")
        print("End the browser")

    return wrapper()


@before_and_after_testing_ui
def test_ui():
    print("Testing UI of the application")

