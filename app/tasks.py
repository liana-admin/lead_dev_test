from app import celery

@celery.task
def async_scrape_and_categorize():
    # To be implemented by the candidate
    pass
