class TitleMixin:
    title = None
    header = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["header"] = self.header
        return context
