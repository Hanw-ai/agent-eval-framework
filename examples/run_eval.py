from agent_eval.runner import BenchmarkRunner


runner = BenchmarkRunner(
    "benchmarks/coding_tasks.jsonl"
)

tasks = runner.load_tasks()

print(
    f"Loaded {len(tasks)} benchmark tasks"
)

for task in tasks:

    print(
        f"Task: {task['id']}"
    )

    print(
        f"Prompt: {task['prompt']}"
    )

    print("-" * 40)
