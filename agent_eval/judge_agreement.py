import json

def calculate_agreement(results):

    total = 0
    agree = 0

    for r in results:

        rule_score = r["rule_score"]
        llm_score = r["llm_score"]

        total += 1

        if (rule_score > 0.5) == (llm_score > 0.5):
            agree += 1

    return {
        "agreement_rate": agree / total
    }
{
  "agreement_rate": 0.86
}
{
  "task_id": "repo_004",
  "rule_score": 1,
  "llm_score": 0.4,
  "reason": "Rule judge only matched keywords."
}

{
  "total_tasks": 35,
  "agreement_rate": 0.83,
  "num_disagreements": 6
}
