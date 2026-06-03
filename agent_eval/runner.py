from agent_eval.runner import BenchmarkRunner
from agent_eval.judge import SimpleJudge


runner = BenchmarkRunner(
    "benchmarks/coding_tasks.jsonl"
)

judge = SimpleJudge()

tasks = runner.load_tasks()

print(
    f"Loaded {len(tasks)} benchmark tasks\n"
)

for task in tasks:

    answer = "sample agent answer"

    result = judge.score(answer)

    print(
        f"Task: {task['id']}"
    )

    print(
        f"Score: {result['score']}"
    )

    print(
        f"Failure Category: {result['failure_category']}"
    )

    print(
        "-" * 40
    )
