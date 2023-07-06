from enum import Enum


class JobStateNames(str, Enum):
    queued = "queued"
    accepted = "accepted"
    finished = "finished"
    error = "error"