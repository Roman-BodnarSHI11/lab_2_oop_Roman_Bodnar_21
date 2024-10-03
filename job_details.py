class JobDetails:
    def __init__(self, position, company):
        self.position = position
        self.company = company

    def get_job_details(self):
        return f"Position: {self.position}, Company: {self.company}"