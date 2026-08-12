import init_django
from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keira")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_drama = Genre.objects.get(name="Dramma")
    genre_drama.name = "Drama"
    genre_drama.save()

    actor_george = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    actor_george.last_name = "Clooney"
    actor_george.save()

    actor_keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_keanu.first_name = "Keanu"
    actor_keanu.last_name = "Reeves"
    actor_keanu.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
