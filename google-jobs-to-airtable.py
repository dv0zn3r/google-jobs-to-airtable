import requests
from pyairtable import Api
from pyairtable import match
from serpapi import GoogleSearch

# Constants for Google Jobs search
GOOGLE_JOBS_SEARCH_PARAMS = {
    "engine": "google_jobs",
    "google_domain": "google.com",
    "q": "postdoctoral new zealand",
    "hl": "en",
    "gl": "us",
    "start": "0",
    "api_key": "",  # Insert serpapi API key
}

# Initialization of Airtable API
api = Api("")  # Insert Airtable  key
table = api.table("", "")  # Insert base ID and table name


def fetch_jobs(params):
    # Send request to retrieve job postings based on specified parameters
    response = requests.get("https://serpapi.com/search.json", params=params)
    # Fetch the 'jobs_results' from response
    return response.json().get('jobs_results', [])


def check_airtable_record_exists(title, university):
    # Checks if a record with the specified title and university exists already
    formula = match({"Title": title, "University": university})
    return table.first(formula=formula)


def construct_data(job, results):
    # constructs a dict comprising job details as well as the relevant URL
    detected_extensions = job.get('detected_extensions', {})
    title = job.get('title')
    university = job.get('company_name')
    data = {
        'Title': title,
        'University': university,
        'Source': job.get('via'),
        'Posted': detected_extensions.get('posted_at'),
        'Description': job.get('description'),
        'Contract': detected_extensions.get('schedule_type'),
        'ID': job.get('job_id'),
        'URL': results.get('search_metadata', {}).get('prettify_html_file'),
    }
    return data, title, university


def process_job(job):
    # process each job, fetching details, constructing the data, and updating or creating an entry
    print(job)
    job_listing_params = {
        "api_key": "",  # Insert serpapi API key
        "engine": "google_jobs_listing",
        "q": job.get('job_id')
    }
    search = GoogleSearch(job_listing_params)
    results = search.get_dict()
    print(results)
    data, title, university = construct_data(job, results)
    existing_entry = check_airtable_record_exists(title, university)
    if existing_entry:
        # if entry exists, update it
        table.update(existing_entry['id'], data)
    else:
        # otherwise, create a new entry
        table.create(data)


def main():
    # Main driver function that fetches the jobs and processes each one
    jobs = fetch_jobs(GOOGLE_JOBS_SEARCH_PARAMS)
    for job in jobs:
        process_job(job)


if __name__ == '__main__':
    main()
