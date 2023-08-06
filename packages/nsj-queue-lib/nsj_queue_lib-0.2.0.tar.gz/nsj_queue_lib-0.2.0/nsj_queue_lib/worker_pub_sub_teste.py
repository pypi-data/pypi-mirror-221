from nsj_queue_lib.worker_pub_sub_base import WorkerPubSubBase, Subscriber
from nsj_queue_lib.settings import logger


class WorkerPubSubTest(WorkerPubSubBase):
    @Subscriber("teste")
    def execute_subscriber_teste(
        self,
        payload: dict[str, any],
        subscription: dict[str, any],
        tarefa: dict[str, any],
        bd_conn,
    ) -> str:
        logger.debug(f"Executando tarefa da assinatura teste. Payload: {payload}")


if __name__ == "__main__":
    WorkerPubSubTest().run()
