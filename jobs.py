class Job:
    company = ""
    job_title = ""
    location = ""
    salary = ""
    date = None
    url = ""

    def __init__(self, company, job_title, location, salary, date, url):
        self.company = company
        self.job_title = job_title
        self.location = location
        self.salary = salary
        self.date = date
        self.url = url


def add_job(job):
    # TODO: Add infrastructure to push job to NoSQL table
    return None
