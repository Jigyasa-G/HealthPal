import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...Try Again",
                "I need more to understand, please rewrite ",
                "What does that mean?"][
        random.randrange(4)]
    return response
