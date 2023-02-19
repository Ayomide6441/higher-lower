from game_data import data
import random
from art import logo, vs


def get_random_account(data_list):
    """Returns a randomly selected account from the given data list"""
    return random.choice(data_list)


def format_account(account):
    """Returns a formatted string of the given account"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def is_guess_correct(guess, a_followers, b_followers):
    """Checks if the user's guess is correct and returns a boolean"""
    return (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)


def play_game():
    """Plays a game of 'Higher Lower'"""
    print(logo)
    score = 0
    account_a = get_random_account(data)
    account_b = get_random_account(data)

    while True:
        if account_a == account_b:
            account_b = get_random_account(data)

        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_account(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        if is_guess_correct(guess, a_followers, b_followers):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        account_a = account_b
        account_b = get_random_account(data)
        print(logo)


if __name__ == '__main__':
    play_game()
