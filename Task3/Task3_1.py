# task3_crawler.py

def top_k_crawl(graph, pagerank_scores, k=5):
    """
    Select top k URLs to crawl based on precomputed PageRank scores.

    Args:
        graph (dict): Keys are URLs, values are lists of outlinks.
        pagerank_scores (dict): Precomputed PageRank scores for each URL.
        k (int): Number of top URLs to select for crawling.

    Returns:
        list: Top k URLs to crawl, sorted by descending PageRank.
    """
    # Keep only URLs that exist in the graph
    urls = [url for url in graph if url in pagerank_scores]

    # Sort by PageRank descending
    urls_sorted = sorted(urls, key=lambda u: pagerank_scores[u], reverse=True)

    return urls_sorted[:k]


if __name__ == "__main__":
    # Example directed web graph
    web_graph = {
        "https://siteA.com": ["https://siteB.com", "https://siteC.com"],
        "https://siteB.com": ["https://siteC.com"],
        "https://siteC.com": ["https://siteA.com"],
        "https://siteD.com": []
    }

    # Precomputed PageRank scores for the URLs
    precomputed_pagerank = {
        "https://siteA.com": 0.35,
        "https://siteB.com": 0.25,
        "https://siteC.com": 0.30,
        "https://siteD.com": 0.10
    }

    # Select top 3 pages to crawl
    top_urls = top_k_crawl(web_graph, precomputed_pagerank, k=3)

    print("Top pages to crawl:", top_urls)
