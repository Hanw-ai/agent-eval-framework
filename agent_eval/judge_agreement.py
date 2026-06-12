def calculate_agreement(results):

    total = 0
    agree = 0

    for r in results:

        rule_score = r["rule_score"]
        llm_score = r["llm_score"]

        total += 1

        if (rule_score > 0.5) == (llm_score > 0.5):
            agree += 1

    if total == 0:
        return {
            "total_tasks": 0,
            "agreements": 0,
            "disagreements": 0,
            "agreement_rate": 0
        }

    return {
        "total_tasks": total,
        "agreements": agree,
        "disagreements": total - agree,
        "agreement_rate": agree / total
    }
