from django.shortcuts import render
from .models import Article

def cluster_view(request):
    clusters = {}
    all_articles = Article.objects.all()
    for cluster_id in set(article.cluster for article in all_articles):
        clusters[cluster_id] = all_articles.filter(cluster=cluster_id)
    return render(request, 'clusters/index.html', {'clusters': clusters})
