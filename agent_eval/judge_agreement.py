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
