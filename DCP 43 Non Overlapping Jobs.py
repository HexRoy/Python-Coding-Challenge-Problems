# Problem
# =====================================================================================================================
# You are given a list of jobs to be done, where each job is represented by a start time and end time.
# Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.
# For example, given the following jobs (there is no guarantee that jobs will be sorted):
# [(0, 6),
# (1, 4),
# (3, 5),
# (3, 8),
# (4, 7),
# (5, 9),
# (6, 10),
# (8, 11)]
# Return:
# [(1, 4),
# (4, 7),
# (8, 11)]


# Solution
# =====================================================================================================================
def longest_job(n):
    """
    longest_job: Find the longest sequence of non overlapping jobs
    :param n: (List(Tuples)) - Contains the start and end time of jobs
    :return: (List(Tuples)) - Contains the longest job sequence
    """
    job_list = []

    for i in range(len(n)):
        temp_job_list = [n[i]]
        end_time = n[i][1]
        for j in range(i, len(n)):
            if n[j][0] >= end_time:
                temp_job_list.append(n[j])
                end_time = n[j][1]
        if len(temp_job_list) > len(job_list):
            job_list = temp_job_list

    return job_list


# Input
# =====================================================================================================================
print(longest_job([(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]))
