def on_success(data = None, message = 'success'):
    if data is not None:
        return data, message
    else:
        on_fail()
def on_fail(message:'failed'):
    return message
def send_file():
    pass