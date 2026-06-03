class TrajectoryAnalyzer:

    def analyze(self, trajectory):

        num_steps = len(trajectory.steps)

        tool_calls = sum(
            1 for step in trajectory.steps
            if step.tool_name
        )

        return {
            "num_steps": num_steps,
            "tool_calls": tool_calls
        }
