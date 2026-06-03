from agent_eval.runner import BenchmarkRunner
from agent_eval.judge import SimpleJudge
from examples.simple_agent import simple_agent
import json

runner = BenchmarkRunner(
    "benchmarks/coding_tasks.jsonl"
)

judge = SimpleJudge()

tasks = runner.load_tasks()

print(
    f"Loaded {len(tasks)} benchmark tasks\n"
)

for task in tasks:

    answer = simple_agent(task["prompt"])

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
   

with open(
    "reports/evaluation_report.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print(
    "Evaluation report saved."
)
    
