from pytest import mark

from .models import Post, Tag


@mark.django_db
def test__no_n_plus_one(client, django_assert_max_num_queries):
    """
    Ensure that n+1 does not affect the blog index page.
    """
    tag_1 = Tag.objects.create(name="Tag 1")

    post_1, created = Post.objects.get_or_create(
        title="title 1",
        slug="slug-1",
        meta_description="post 1",
        content="post 1",
        published=True,
    )
    post_1.tags.add(tag_1)

    with django_assert_max_num_queries(5):
        response = client.get("/")
        assert response.status_code == 200

    tag_2 = Tag.objects.create(name="Tag 2")
    post_2, created = Post.objects.get_or_create(
        title="title 2",
        slug="slug-2",
        meta_description="post 2",
        content="post 2",
        published=True,
    )
    post_2.tags.add(tag_2)

    with django_assert_max_num_queries(5):
        response = client.get("/")
        assert response.status_code == 200
