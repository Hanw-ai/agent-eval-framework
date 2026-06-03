from agent_eval.failures import FAILURE_CATEGORIES


class SimpleJudge:

    def score(self, answer):

        if len(answer.strip()) == 0:

            return {
                "score": 0,
                "success": False,
                "failure_category": "incomplete_task"
            }

        return {
            "score": 1,
            "success": True,
            "failure_category": "success"
        }
