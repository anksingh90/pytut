import random
import statistics

def simulate_coin_flips(num_flips):
    """Simulates coin flips and calculates the empirical probability of heads."""
    results = [random.choice(["H", "T"]) for _ in range(num_flips)]
    heads_count = results.count("H")
    probability_heads = heads_count / num_flips
    return probability_heads

def simulate_dice_rolls(num_rolls, num_sides=6):
    """Simulates dice rolls and calculates the empirical probability of each outcome."""
    results = [random.randint(1, num_sides) for _ in range(num_rolls)]
    probabilities = {}
    for side in range(1, num_sides + 1):
      probabilities[side] = results.count(side)/num_rolls
    return probabilities

def simulate_card_draws(num_draws):
    """Simulates drawing cards from a standard deck (without replacement)."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

    draws = random.sample(deck, num_draws)  # Sample without replacement
    return draws

def main():
    while True:
        print("\nProbability Simulator")
        print("1. Simulate Coin Flips")
        print("2. Simulate Dice Rolls")
        print("3. Simulate Card Draws")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_flips = int(input("Enter the number of coin flips: "))
            probability = simulate_coin_flips(num_flips)
            print(f"Empirical probability of heads: {probability:.4f}")
        elif choice == "2":
            num_rolls = int(input("Enter the number of dice rolls: "))
            num_sides = int(input("Enter the number of sides on the die(default 6): ") or 6)
            probabilities = simulate_dice_rolls(num_rolls,num_sides)
            for side, prob in probabilities.items():
                print(f"Empirical probability of rolling a {side}: {prob:.4f}")
        elif choice == "3":
            num_draws = int(input("Enter the number of cards to draw: "))
            if num_draws > 52:
                print("You can't draw more than 52 cards from a standard deck.")
            else:
                draws = simulate_card_draws(num_draws)
                print("Cards drawn:")
                for card in draws:
                    print(card)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()