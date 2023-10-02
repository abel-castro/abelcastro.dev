import random

import faker
from blog.models import Post, Tag
from django.core.management.base import BaseCommand
from mdgen import MarkdownPostProvider


class Command(BaseCommand):
    help = "Creates demo Posts and Tags"

    def add_arguments(self, parser):
        parser.add_argument("amount_post", type=int)
        parser.add_argument(
            "--clean",
            action="store_true",
            help="Delete all existing data",
        )

    def handle(self, *args, **options):
        amount_post = options["amount_post"]
        clean = options["clean"]

        if clean:
            Post.objects.all().delete()
            Tag.objects.all().delete()

        fake = faker.Faker()
        fake.add_provider(MarkdownPostProvider)

        tags = []
        for i in range(5):
            tags.append(Tag(name=fake.color_name()))

        tags = Tag.objects.bulk_create(tags)

        for p in range(amount_post):
            post = Post.objects.create(
                title=fake.sentence(),
                slug=fake.slug(),
                meta_description=fake.paragraph(nb_sentences=1),
                content=fake.post(size="medium"),
                date=fake.date_object(),
                published=True,
            )
            post.tags.set(random.choices(tags))
