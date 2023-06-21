from ..models import Worker
from user.models import UserInfo

class CreateWorker:
    def create(self, body):
        try:
            user_info = UserInfo.objects.filter(contact=body["user"]["phone"]).first()
            worker = Worker(user_info=user_info)
            worker.save()
            return worker
        except Exception as e:
            raise Exception(str(e))