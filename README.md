# Project Title: Job Listing Fetcher

This Python project fetches job listings from Google Jobs using SerpApi and stores this data in an Airtable database. It ensures any positions already tracked are updated, and new job listings are added, preventing duplication.

## Getting Started

These instructions will guide you in getting a copy of the project up and running on your local machine. 

### Prerequisites

Ensure you have the following installed:

* Python 3.x
* An editor such as PyCharm or Visual Studio Code

### Dependencies

This project uses the following Python libraries:

* `requests`
* `pyairtable`
* `serpapi`

See [requirements.txt](requirements.txt) file. Install them using pip:

```sh
pip install -r requirements.txt
```

### Configuration

To run the script, you will need to provide the following:

* SerpApi API key
* Airtable API key and table details
* Customize the search parameters for job listings in `GOOGLE_JOBS_SEARCH_PARAMS`

## Usage

After setup and configuration, run the script:

```sh
python google-job-to-airtable.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
