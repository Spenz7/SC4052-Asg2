Task 3.1 -- Selecting Top Pages to Crawl Using PageRank
===========================================

Description
-----------

This program selects the **top k URLs to crawl** from a small directed web graph using **precomputed PageRank scores**.

It demonstrates an **authority-based crawling strategy**, where pages with higher PageRank are prioritized as they are more likely to contain important and useful content.

How It Works
------------

-   Input:
    -   A web graph (dictionary: URL -> list of outlinks)
    -   Precomputed PageRank scores (dictionary: URL -> score)
-   Output:
    -   Top k URLs sorted by descending PageRank

Setup & Run
-----------

1.  Clone the repository or download the file:

```bash
git clone https://github.com/yourusername/task3_crawler.git\
cd task3_crawler
```

2.  Run the script:

```bash
python task3_crawler.py
```

Example Output
--------------

```bash
Top pages to crawl: ['https://siteA.com', 'https://siteC.com', 'https://siteB.com']
```

Notes
-----

-   This is a **small illustrative example** for demonstration.
-   In practice, PageRank scores would be computed on a large graph (see Task 2).
