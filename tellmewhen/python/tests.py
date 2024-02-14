import tell
import requests

def tell_load():
    """Check config file is loaded correctly."""
    file = tell.load("me.toml")
    print(f"Config read success: \n\n{file}\n\n")

def tell_post():
    """Check that requests are in the correct format and that the server responds."""
    settings = {'tele': 
                           {'chat_id': '', 
                            'bot_token': ''}
               }
    test_tell = ['This is a test', 't', '']
    status = tell.post(test_tell, settings)
    for call, response in status.items():
        if response == 404:
            print(f"{call}: OK")
        else:
            print(f"{call}: Fail")

