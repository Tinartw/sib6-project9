import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cponqu1r01qj9etvb180cponqu1r01qj9etvb18g")

    news = finnhub_client.general_news('general', min_id=0)

    return news
