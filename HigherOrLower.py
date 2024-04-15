# import click
import random

from Art import logo, vs
from GameData import data


def get_random_account():
    return random.choice(data)


def format_account(account):
    name = account["name"]
    job = account['description']
    country = account['country']
    return f"{name}, a {job} from {country}"


def check_answer(a_follower_count, b_follower_count, user_guess):
    if a_follower_count > b_follower_count:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


def game():
    print(logo)
    game_continue = True
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    while game_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_account(account_a)}")
        print(f"{account_a['follower_count']}")
        print(vs)
        print(f"with B: {format_account(account_b)}")
        print(f"{account_b['follower_count']}")
        user_guess = input("Which has more Insta followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(a_follower_count, b_follower_count, user_guess)

        # click.clear()
        # print(logo)
        if is_correct:
            score += 1
            print(f"Correct! Current score: {score}")
        else:
            game_continue = False
            print("Sorry! That was incorrect.")
            print(f"Game Over. Final Score is {score}")


game()
