import pandas as pd
import random

def load_demons(filename):
    return pd.read_csv(filename)

def summon_demon(demons_df, filter_criteria=None):
    if filter_criteria:
        filtered_demons = demons_df.query(filter_criteria)
        if filtered_demons.empty:
            return None
        return filtered_demons.sample()
    return demons_df.sample()

def summoning_history(history):
    print("\nSummoning History:")
    if history:
        for i, demon in enumerate(history, start=1):
            print(f"{i}. {demon['Name']} ({demon['Rank']})")
    else:
        print("No demons have been summoned yet.")

def main():
    demons_df = load_demons('data/demons.csv')
    summoned_demons = []

    while True:
        print("\n1. Summon a demon\n2. View summoning history\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filter_criteria = input("Enter filter criteria (e.g., 'Rank == \"High\"') or press enter to skip: ")
            demon = summon_demon(demons_df, filter_criteria if filter_criteria else None)
            if demon is not None:
                print("\nYou have summoned {} ({}):".format(demon.iloc[0]['Name'], demon.iloc[0]['Rank']))
                print("{}\n".format(demon.iloc[0]['Description']))
                summoned_demons.append(demon.iloc[0])
            else:
                print("No demon meets the criteria or no demons left to summon.")
        elif choice == '2':
            summoning_history(summoned_demons)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
