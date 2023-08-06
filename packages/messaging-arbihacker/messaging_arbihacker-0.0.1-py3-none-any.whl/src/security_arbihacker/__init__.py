from celery import Celery
from kombu.common import Broadcast


class ArbiCelery(Celery):
    USER_Q = "user"
    DATA_Q = "data"
    EVENT_Q = "event"
    TASK_Q = "task"
    NOTIFICATION_Q = "notification"
    UPDATE_Q = "update"

    def __init__(
        self,
        main: str | None = None,
        broker: str | None = None,
        backend: str | None = None,
        **kwargs,
    ):
        super().__init__(main, broker=broker, backend=backend, **kwargs)
        self.conf.task_queues = (Broadcast(ArbiCelery.UPDATE_Q),)
        self.conf.task_routes = {
            f"{ArbiCelery.USER_Q}.*": {"queue": ArbiCelery.USER_Q},
            f"{ArbiCelery.DATA_Q}.*": {"queue": ArbiCelery.DATA_Q},
            f"{ArbiCelery.EVENT_Q}.*": {"queue": ArbiCelery.EVENT_Q},
            f"{ArbiCelery.TASK_Q}.**": {"queue": ArbiCelery.TASK_Q},
            f"{ArbiCelery.NOTIFICATION_Q}.*": {"queue": ArbiCelery.NOTIFICATION_Q},
            f"{ArbiCelery.UPDATE_Q}.*": {
                "queue": ArbiCelery.UPDATE_Q,
                "exchange": ArbiCelery.UPDATE_Q,
            },
        }
