from openai import OpenAI
import json


class OpenAIJudge:

    def __init__(self, api_key):

        self.client = OpenAI(
            api_key=api_key
        )

    def score(
        self,
        task_prompt,
        expected,
        answer
    ):

        response = self.client.responses.create(

            model="gpt-4.1-mini",

            input=f"""
Task:
{task_prompt}

Expected:
{expected}

Agent Answer:
{answer}

Evaluate the agent answer.

Return JSON only.

{
  "score": float,
  "failure_category": string,
  "explanation": string
}

Valid failure categories:

- success
- incorrect_reasoning
- tool_misuse
- context_loss
- incomplete_task
- hallucinated_action
"""
        )

       return json.loads(
    response.output_text
)
