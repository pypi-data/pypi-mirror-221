import abc

from nsj_gcf_utils.json_util import json_loads

from nsj_queue_lib.exception import SubscriberNotRegistered
from nsj_queue_lib.settings import logger
from nsj_queue_lib.worker_base import WorkerBase


class Subscriber:
    METHOD_SUBSCRIBER_DICT = {}

    def __init__(self, subscriber_id: str) -> None:
        self.subscriber_id = subscriber_id

    def __call__(self, func):
        Subscriber.METHOD_SUBSCRIBER_DICT[self.subscriber_id] = func
        return func


class WorkerPubSubBase(WorkerBase, abc.ABC):
    def execute(self, payload: str, tarefa: dict[str, any], bd_conn) -> str:
        logger.info(f"Executando a tarefa PubSub de ID: {tarefa['id']}")
        logger.debug(f"Dados da tarefa: {tarefa}")

        # Recuperando os dados da tarefa
        payload = json_loads(payload)
        subscription = payload["subscription"]
        subscriber_id = subscription["id"]

        # Recuperando a função registrada para subscriber_id
        if subscriber_id not in Subscriber.METHOD_SUBSCRIBER_DICT:
            raise SubscriberNotRegistered(
                f"Subscriber '{subscriber_id}' não registrado."
            )

        # Executando o método registrado para o subscriber_id
        return Subscriber.METHOD_SUBSCRIBER_DICT[subscriber_id](
            self,
            payload,
            subscription,
            tarefa,
            bd_conn,
        )
