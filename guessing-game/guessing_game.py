import random

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
    
if __name__ == '__main__':
    
    total_tentativas = 5
    n_secret = random.randrange(0, 100)
    
    for rodada in range (1, total_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_tentativas))
        guess = input("Digite um palpite entre 1 e 100: {}    ".format(n_secret))
        if (int(guess) < 1 or int(guess) > 100):
            print("Você deve digitar um número de 0 a 100")
            continue 
        if divination(n_secret, int(guess)) == 'lower':
            print("Você digitou {}, the secret number is lower" .format(guess))
        elif divination(n_secret, int(guess)) == 'higher':
            print("Você digitou {}, the secret number is higher".format(guess))
        elif divination(n_secret, int(guess)) == 'Congrats':
            print("Congrats, Você ganhou")
            break