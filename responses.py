import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    elif p_message == 'hi':
        return 'Oh kawai kotto'
    elif message == 'roll':
        return str(random.randint(1, 6))
    elif p_message == '!help':
        return '`If you have any concern about the bot, contact to senpaix#9980`'
    elif "favorite anime" in p_message:
        return "It's hard to pick just one favorite anime, but if I had to choose, I'd say Naruto!"
    elif "understand anime" in p_message:
        return "Believe it! Anime can be a lot of fun, and there's something out there for everyone. Why not give it a try?"
    elif "library" in p_message:
        return "Did you hear about the anime character who went to the library? He came out with a whole stack of manga!"
    elif "cross the road" in p_message:
        return "Why did the anime character cross the road? To get to the other side of the plot!"
    elif "worth" in p_message and "anime" in p_message:
        return "The anime industry is huge! In 2020, it was estimated to be worth over $24 billion worldwide."
    else:
        return "I'm sorry, I don't understand. If you have any concerns about the bot, please contact senpaix#9980."
