from dataclasses import dataclass
from typing import List


@dataclass
class AgentStep:
    step_id: int
    thought: str
    tool_name: str | None
    tool_input: str | None
    tool_output: str | None


@dataclass
class AgentTrajectory:
    task_id: str
    prompt: str
    final_answer: str
    steps: List[AgentStep]
