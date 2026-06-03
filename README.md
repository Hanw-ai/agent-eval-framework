# Agent Evaluation Framework
A lightweight framework for evaluating LLM agents across task success, tool-use correctness, trajectory quality, and failure modes.

Inspired by real-world challenges in agent reliability, benchmark evaluation, and feedback-driven improvement.

## Motivation

LLM agents often fail in ways that traditional metrics cannot capture.

Common failure modes include:

- Tool misuse
- Context loss
- Hallucinated actions
- Incomplete task execution
- Incorrect reasoning

This project provides a simple framework for systematically evaluating and improving agent performance.

---

## Architecture

```text
Benchmark Tasks
      ↓
Agent Execution
      ↓
Trajectory Collection
      ↓
LLM Judge
      ↓
Failure Categorization
      ↓
Evaluation Report
```

---

## Features

### Benchmark Runner

Run benchmark datasets across coding, reasoning, and agent tasks.

### Agent Trajectory Schema

Track intermediate reasoning, tool calls, and final outputs.

### Failure Categorization

Supported categories:

- tool_misuse
- context_loss
- hallucinated_action
- incomplete_task
- incorrect_reasoning
- format_error

### LLM Judge

Evaluate outputs using rubric-based scoring.

---

## Example

```python
from agent_eval.runner import BenchmarkRunner

runner = BenchmarkRunner(
    "benchmarks/coding_tasks.jsonl"
)

tasks = runner.load_tasks()

print(tasks)
```

## Example Output

```text
Loaded 3 benchmark tasks

Task: task_001
Score: 1
Failure Category: success
----------------------------------------

Task: task_002
Score: 1
Failure Category: success
----------------------------------------

Task: task_003
Score: 1
Failure Category: success
----------------------------------------
```

## Project Structure

```text
agent_eval/
├── schema.py
├── failures.py
├── judge.py
└── runner.py

benchmarks/
└── coding_tasks.jsonl

examples/
└── run_eval.py
```

## Current Status

Implemented:

- Benchmark Runner
- Agent Trajectory Schema
- Failure Taxonomy
- Simple Judge
- Example Evaluation Workflow

In Progress:

- GPT-based LLM Judge
- Trajectory Analysis
- Evaluation Dashboard

## Roadmap

- GPT-based LLM Judge
- Agent Trajectory Analysis
- HTML Evaluation Dashboard
- Repository-Level Coding Benchmarks
- Multi-Agent Evaluation Support

## Why This Matters

Modern AI systems are increasingly agentic.

Improving agent reliability requires:

- Better evaluation
- Better failure analysis
- Better feedback loops

## Future Directions

Potential extensions include:

- Repository-level coding benchmarks
- Multi-agent workflow evaluation
- Tool-use correctness scoring
- Long-horizon task success metrics
- Human + LLM hybrid evaluation

This project explores the infrastructure needed to support those workflows.
