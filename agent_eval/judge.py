class SimpleJudge:

    def score(self, answer):

        if len(answer.strip()) == 0:
            return {
                "score": 0,
                "success": False
            }

        return {
            "score": 1,
            "success": True
        }
