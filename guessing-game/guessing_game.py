print("*********************************")
print("**Welcome to the Guessing Game!**")
print("*********************************")

def divination(n_secret, guess):
    if (n_secret != guess):
        if guess > n_secret:
            return 'lower'
        elif guess < n_secret:
            return 'higher'
    else: return 'Congrats'