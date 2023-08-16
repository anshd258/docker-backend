import uuid
from gig.models.job import Job

def GenerateLink(jobid):
    try:
        print('nhiiiiiiiiii')
        unique_link = str(uuid.uuid4())
        while Job.objects.filter(unique_link=unique_link).exists():
            unique_link = str(uuid.uuid4())
        job=Job.objects.get(pk=jobid)
        job.unique_link = unique_link
        job.save()
        print(unique_link)
        return unique_link
    except Exception as e:
        print(str(e))