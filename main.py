from pet import Pet

def main():
    buddy = Pet("Buddy")

    buddy.get_status()
    buddy.eat()
    buddy.sleep()
    buddy.play()
    buddy.train("roll over")
    buddy.train("sit")
    buddy.get_status()
    buddy.show_tricks()

if __name__ == "__main__":
    main()