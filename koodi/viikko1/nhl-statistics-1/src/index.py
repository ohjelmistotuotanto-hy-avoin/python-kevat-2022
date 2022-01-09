from statistics import Statistics


def main():
    stats = Statistics()
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top_scorers(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top scorers:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
