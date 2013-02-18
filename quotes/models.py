from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)
    pubdate = models.DateTimeField('date published', auto_now=True)

    def __unicode__(self):
        n = 10
        words = self.text.split()
        text = ' '.join(words[:n]) + ('...' if len(words) > n else '')
        return text
