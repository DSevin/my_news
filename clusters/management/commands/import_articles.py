from django.core.management.base import BaseCommand
from clusters.models import Article
import pandas as pd

class Command(BaseCommand):
    help = 'Load articles from a CSV file into the database'

    def handle(self, *args, **options):
        df = pd.read_csv('clustered_news_articles.csv')
        for _, row in df.iterrows():
            Article.objects.create(
                title=row['Title'],
                url=row['URL'],
                content=row['Content'],
                cluster=row['Cluster']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded articles into the database'))
