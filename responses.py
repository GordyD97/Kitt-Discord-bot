import random

def get_response(message: str) -> str:
    p_message = message.lower() 
    
    if p_message == "hello":
        return 'Hey there!'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    
        return 'I didnt understand what you wrote, try typing "!help".'
    
    # //////////////////////////////////////////////////////////////////////////////////

    def get_response(user_input: str) -> str: 
        raise NotImplementedError('missing code...')