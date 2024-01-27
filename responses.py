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
    



    # /////////////////////////////////////////////////////////////////////return statements under //////////////////////////////////

        return choice(['I do not understand...',
                       'What the hell are you talking about?',
                       'ummm......Come again loser?',
                       'Um, hello? Do you speak English? Because Im not getting it.',
                       'Wow, are you trying to type alien or something? Because Im not fluent in that.',
                       'Are you even typing in human right now? Because Im lost.',
                       'Did you forget to switch to English mode? Because Im not picking up what youre putting down',
                       'Is this a secret code or are you just messing with me? Because Im not cracking it',
                       'Okay, someone get me a translator cause Im lost in the Bermuda Triangle of confusion',
                       'Congratulations, youve officially entered the Lost in Translation zone. I have no idea what youre saying.',
                       'Is this a pop quiz in another language? Cause I didnt get programmed for that.',
                       'I must have missed the memo on typing idiot today, cause Im not fluent',
                       'Sorry, I left my decoder ring on my other hard drive. What language are we typing now',
                       'Hey, did we suddenly switch to a foreign film? Cause Im not following the plot.',
                       'Are we playing charades or something? Cause your message isnt coming through.',
                       'Do I need a secret password to understand you? Cause Im not in the loop',
                       'Is this some kind of prank? Cause Im not laughing, Im just confused.',
                       'Did you accidentally switch to wingdings or something? Cause Im not picking it up',
                       'Okay, is this a new slang term I havent heard of yet? Cause Im not hip to it',
                       'Hold up, did you just pull out the Thesaurus for that? Cause Im not fluent in fancy talk',
                       'Are you speaking in riddles now? Cause Im not in the mood for a CPU teaser',
                       ])