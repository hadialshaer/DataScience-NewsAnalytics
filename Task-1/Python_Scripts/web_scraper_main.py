from ArticleScraperClass import ArticleScraper
from FileUtilityClass import FileUtility
from SiteParserClass import SitemapParser


def main():
    """
    Main function to coordinate the sitemap parsing, article scraping, and file saving processes.
    """
    # Initialize the sitemap index URL
    sitemap_index_url = "https://www.almayadeen.net/sitemaps/all.xml"

    try:
        # Create a SitemapParser object with the index URL
        print("Initializing SitemapParser...")
        sitemap_parser = SitemapParser(sitemap_index_url)
        print("SitemapParser initialized successfully.")
    except Exception as e:
        # Handle any errors that occur during initialization
        print(f"Error initializing SitemapParser: {e}")
        return  # Exit the function if initialization fails

    try:
        # Fetch the list of monthly sitemap URLs from the sitemap index
        print("Fetching monthly sitemap URLs...")
        monthly_sitemap_urls = sitemap_parser.fetch_sitemap_index()
        print(f"Fetched {len(monthly_sitemap_urls)} monthly sitemaps.")
    except Exception as e:
        # Handle errors related to fetching the sitemap index
        print(f"Error fetching monthly sitemap URLs: {e}")
        return  # Exit the function if fetching URLs fails

    total_article_counter = 0  # Counter for the total number of articles
    overall_article_limit = 12000  # Overall article limit across all months

    # Filter the sitemaps to process 2024 first, then 2023, and so on if needed
    monthly_sitemap_urls.sort(reverse=True)  # Sort descending by year and month
    filtered_sitemap_urls = []

    # First, add all the sitemaps from the year 2024
    for url in monthly_sitemap_urls:
        if '2024' in url:
            filtered_sitemap_urls.append(url)

    # Next, add all the sitemaps from the year 2023
    for url in monthly_sitemap_urls:
        if '2023' in url:
            filtered_sitemap_urls.append(url)

    # Calculate the maximum number of articles to scrape from each sitemap
    # If there are more than 12000 articles in total, divide this number
    total_sitemaps = len(filtered_sitemap_urls)
    if total_sitemaps > 0:
        articles_per_sitemap = overall_article_limit // total_sitemaps
    else:
        articles_per_sitemap = overall_article_limit  # Fallback if no sitemaps are available

    # Process each monthly sitemap URL
    for monthly_sitemap_url in filtered_sitemap_urls:
        if total_article_counter >= overall_article_limit:
            break  # Stop if the overall article limit has been reached

        try:
            # Extract the year and month from the sitemap URL
            year, month = sitemap_parser.extract_year_month_from_url(monthly_sitemap_url)
            print(f"Processing sitemap for {year}-{month:02d}...")

            # Fetch all article URLs from this monthly sitemap
            article_urls = sitemap_parser.fetch_article_urls(monthly_sitemap_url)
            print(f"Fetched {len(article_urls)} article URLs from {monthly_sitemap_url}.")
        except Exception as e:
            # Handle errors related to processing each sitemap
            print(f"Error processing sitemap {monthly_sitemap_url}: {e}")
            continue  # Skip to the next sitemap if there's an error

        articles = []  # List to store Article objects for the current month
        monthly_article_counter = 0  # Counter for articles scraped in the current month

        # Process each article URL
        for article_url in article_urls:
            if monthly_article_counter >= articles_per_sitemap:
                break  # Stop if the monthly limit is reached

            if total_article_counter >= overall_article_limit:
                break  # Stop if the overall article limit is reached

            try:
                # Create an ArticleScraper and scrape the article
                scraper = ArticleScraper()
                print(f"Scraping article: {article_url}")
                article = scraper.scrape_article(article_url)
                if article:
                    articles.append(article)
                    monthly_article_counter += 1
                    total_article_counter += 1
                    print(f"Total articles scraped so far: {total_article_counter}")
                    print(f"Article content: {article}")  # Print scraped article data
                else:
                    print(f"No content found for article {article_url}.")
            except Exception as e:
                # Handle errors related to scraping individual articles
                print(f"Error scraping article {article_url}: {e}")

        # Save the articles for the current month to a JSON file
        if articles:
            try:
                FileUtility.save_articles_to_json(articles, year, month)
                print(f"Saved {len(articles)} articles for {year}-{month:02d}.")
            except IOError as e:
                # Handle errors related to file I/O when saving articles
                print(f"Error saving articles for {year}-{month:02d}: {e}")

    # Print the total number of articles scraped after processing all sitemaps
    print(f"Scraping completed. Total articles scraped: {total_article_counter}")


if __name__ == "__main__":
    main()
