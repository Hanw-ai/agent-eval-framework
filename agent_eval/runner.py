import json


class BenchmarkRunner:

    def __init__(self, benchmark_path):
        self.benchmark_path = benchmark_path

    def load_tasks(self):

        tasks = []

        with open(self.benchmark_path) as f:

            for line in f:

                if line.strip():

                    tasks.append(
                        json.loads(line)
                    )

        return tasks
