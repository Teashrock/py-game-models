import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_data:
        players = json.load(player_data)
        for player_name, player_contents in players.items():
            Player.objects.create(
                nickname=player_name,
                email=player_contents["email"],
                bio=player_contents["bio"],
                race=Race.objects.get_or_create(
                    name=player_contents["race"]["name"],
                    description=player_contents["race"]["description"],
                )[0],
                guild=Guild.objects.get_or_create(
                    name=player_contents["guild"]["name"]
                )[0]
            )
            for skill in player_contents["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get_or_create(
                        name=player_contents["race"]["name"],
                        description=player_contents["race"]["description"],
                    )[0]
                )


if __name__ == "__main__":
    main()
