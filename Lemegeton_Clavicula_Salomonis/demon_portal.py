import pandas as pd
import random 

def load_demons(filename):
    """
    Loads the demon data from a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(filename)

def summon_demon(demons_df):
    """
    Selects a random demon from the DataFrame.
    """
    return demons_df.sample()

def main():
    """
    Main interface for summoning demons. It loads the demons and allows
    the user to summon them randomly.
    """
    # Load the demons from the CSV file
    demons_df = load_demons('data/demons.csv')
    
    while True:
        input("Press enter to summon a demon...")
        demon = summon_demon(demons_df)
        
        # Display the summoned demon's information
        print("\nYou have summoned {} ({}):".format(demon.iloc[0]['Name'], demon.iloc[0]['Rank']))
        print("{}\n".format(demon.iloc[0]['Description']))
        
        # Ask the user if they want to summon another demon
        if input("Summon another? (y/n): ").lower() != 'y':
            break

if __name__ == '__main__':
    main()
