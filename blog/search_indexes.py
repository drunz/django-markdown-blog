import datetime
from haystack import indexes
from blog.models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    date = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return Post

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date__lte=datetime.datetime.now())
