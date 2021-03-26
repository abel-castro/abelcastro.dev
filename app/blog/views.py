from django.views.generic import DetailView, ListView, TemplateView

from .models import Post
from .constants import BLOG_META_DESCRIPTION


class BlogView(ListView):
    template_name = "blog.html"
    model = Post
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "Abel Castro Blog"
        context["meta_description"] = BLOG_META_DESCRIPTION
        return context


class PostView(DetailView):
    template_name = "post.html"
    model = Post
    queryset = Post.objects.filter(published=True).prefetch_related("tags")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        post = self.get_object()
        context["page_title"] = f"{post.title} - Abel Castro"
        context["meta_description"] = post.meta_description
        return context


class AboutMeView(TemplateView):
    template_name = "about_me.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "About me - Abel Castro"
        context["meta_description"] = BLOG_META_DESCRIPTION
        return context
