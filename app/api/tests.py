import pytest
from pytest import mark

from api.models import APIToken
from blog.models import Post, Tag


@pytest.fixture
def api_token(db):
    raw = "test-secret-token"
    token = APIToken(name="test")
    token.set_token(raw)
    token.save()
    return raw, token


@mark.django_db
class TestPostCreateAuth:
    url = "/api/posts/"
    payload = {"title": "My Draft", "content": "# Hello"}

    def test_no_token_returns_403(self, client):
        response = client.post(self.url, self.payload, content_type="application/json")
        assert response.status_code == 403

    def test_wrong_token_returns_403(self, client):
        response = client.post(
            self.url,
            self.payload,
            content_type="application/json",
            HTTP_AUTHORIZATION="Bearer wrong-token",
        )
        assert response.status_code == 403

    def test_valid_token_returns_201(self, client, api_token):
        raw, _ = api_token
        response = client.post(
            self.url,
            self.payload,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {raw}",
        )
        assert response.status_code == 201


@mark.django_db
class TestPostCreate:
    url = "/api/posts/"

    def _post(self, client, raw_token, payload):
        return client.post(
            self.url,
            payload,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {raw_token}",
        )

    def test_creates_as_draft(self, client, api_token):
        raw, _ = api_token
        self._post(client, raw, {"title": "Draft Post", "content": "body"})
        post = Post.objects.get(slug="draft-post")
        assert post.published is False

    def test_slug_generated_from_title(self, client, api_token):
        raw, _ = api_token
        response = self._post(client, raw, {"title": "Hello World", "content": "body"})
        assert response.data["slug"] == "hello-world"

    def test_duplicate_title_gets_suffix(self, client, api_token):
        raw, _ = api_token
        Post.objects.create(
            title="Clash", slug="clash", content="x", meta_description="", published=False, date="2024-01-01"
        )
        response = self._post(client, raw, {"title": "Clash", "content": "body"})
        assert response.data["slug"] == "clash-1"

    def test_tags_are_created_if_new(self, client, api_token):
        raw, _ = api_token
        self._post(client, raw, {"title": "Tagged", "content": "body", "tags": ["python", "django"]})
        post = Post.objects.get(slug="tagged")
        assert set(post.tags.values_list("name", flat=True)) == {"python", "django"}

    def test_existing_tags_are_reused(self, client, api_token):
        raw, _ = api_token
        Tag.objects.create(name="python")
        self._post(client, raw, {"title": "Reuse Tags", "content": "body", "tags": ["python"]})
        assert Tag.objects.filter(name="python").count() == 1

    def test_meta_description_defaults_to_empty(self, client, api_token):
        raw, _ = api_token
        self._post(client, raw, {"title": "No Meta", "content": "body"})
        post = Post.objects.get(slug="no-meta")
        assert post.meta_description == ""

    def test_get_still_works_without_auth(self, client):
        response = client.get(self.url)
        assert response.status_code == 200
