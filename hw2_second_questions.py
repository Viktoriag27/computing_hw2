############################################
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#############################################

cv = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
      {'user': 'jane', 'jobs': ['finance', 'software']}]

# 4)
def has_experience_as(cvs: list, job_title: str) -> list:
    """
    Fuction that identifies the names of each user who has worked as job tittle.
    That has two parameters:
    1. A list of CV's.
    2. A string (job_title)  
    Finally, it returns a list of strings containing the names of each user.
    """
    names = []
    for i in cvs:
        if job_title in i['jobs']:
            names.append(i['user'])
    return list(set(names))

print(has_experience_as(cv, 'finance'))

# 5)
def job_counts(cvs: list) -> dict:
    """
    That function returns a dictionary where the keys are the job titles
    and values are the numbers of users that have done that job.
    Parameter:
    1. A list of CV's
    """
    dict1 = {}
    for i in cvs:
        for j in i["jobs"]:
            if j in dict1:
                dict1[j] += 1
            else:
                dict1[j] = 1
    return dict1

print(job_counts(cv))

# 6)
def most_popular_job(cvs: list) -> tuple:
    """
    This function returns a tuple representing the title of the most popular job and the number of times it was held. It takes one parameter:
    Parameter:
    1. A list of CVs.
    Inside this function, another function called job_counts() is used, which was created earlier.
    """
    dict1 = job_counts(cvs)
    max1 = max(dict1.values())
    jobs = [i for i, j in dict1.items() if j == max1]
    return (jobs, max1)

print(most_popular_job(cv))
        

