from basic_analytics_tracker.mixins import TrackingMixin
from blog.constants import BLOG_META_DESCRIPTION
from blog.models import Post
from django.views.generic import DetailView, ListView, TemplateView


class PostsBaseView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    paginate_by = 3


class PostsListView(TrackingMixin, PostsBaseView):
    template_name = "post_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "Abel Castro Blog"
        context["meta_description"] = BLOG_META_DESCRIPTION
        return context


class PostSearchView(PostsBaseView):
    template_name = "post_search.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        search_term = self.request.GET.get("search_term", "")
        queryset = self.get_queryset()

        if search_term:
            queryset = queryset.filter(title__contains=search_term) | queryset.filter(
                content__contains=search_term
            )

        context["object_list"] = queryset
        return context


class PostsLoadMoreView(PostsBaseView):
    template_name = "load_more_posts.html"


class PostDetailView(TrackingMixin, DetailView):
    template_name = "post_detail.html"
    model = Post
    queryset = Post.objects.filter(published=True).prefetch_related("tags")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        post = self.get_object()
        context["page_title"] = f"{post.title} - Abel Castro"
        context["meta_description"] = post.meta_description
        return context


class AboutMeView(TrackingMixin, TemplateView):
    template_name = "about_me.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "About me - Abel Castro"
        context["meta_description"] = BLOG_META_DESCRIPTION
        return context


class PrivacyPolicyView(TrackingMixin, TemplateView):
    template_name = "privacy_policy.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "Privacy Policy - Abel Castro"
        context["meta_description"] = BLOG_META_DESCRIPTION
        return context
