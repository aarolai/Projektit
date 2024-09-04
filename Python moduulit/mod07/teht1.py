seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

user_input = int(input("Syötä kuukauden numero: "))


print(f"Kuukauden {user_input} vuodenaika on {seasons[user_input-1]}")
