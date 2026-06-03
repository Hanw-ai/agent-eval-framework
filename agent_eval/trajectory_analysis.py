class TrajectoryAnalyzer:

    def analyze(self, trajectory):

        num_steps = len(trajectory.steps)

        tool_calls = sum(
            1
            for step in trajectory.steps
            if step.tool_name
        )

        tool_use_rate = (
            tool_calls / num_steps
            if num_steps > 0
            else 0
        )

        reasoning_depth = num_steps

        failure_stage = self.identify_failure_stage(
            trajectory
        )

        return {

            "num_steps": num_steps,

            "tool_calls": tool_calls,

            "tool_use_rate": round(
                tool_use_rate,
                2
            ),

            "reasoning_depth": reasoning_depth,

            "failure_stage": failure_stage
        }

    def identify_failure_stage(
        self,
        trajectory
    ):

        for step in trajectory.steps:

            if step.tool_name and not step.tool_output:

                return "tool_use"

        return "reasoning"
