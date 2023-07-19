from vbfsharedmodels.models.JobState import JobState


class JobStateCountdown(JobState):
    jobs_to_compute: int
