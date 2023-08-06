from nsj_queue_lib.worker_base import WorkerBase

# from settings import logger


class WorkerFilaTeste(WorkerBase):
    def execute(self, payload: str, tarefa: dict[str, any], bd_conn) -> str:
        print(tarefa)
        raise Exception("erro de teste")
        # return "Mensagem de sucesso personalizada!"


if __name__ == "__main__":
    WorkerFilaTeste().run()
