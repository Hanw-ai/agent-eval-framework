def compare_models(model_results):
    summary = []

    for model_name, results in model_results.items():
        scores = [r["score"] for r in results]
        success_count = sum(1 for r in results if r.get("success"))

        summary.append({
            "model": model_name,
            "avg_score": round(sum(scores) / len(scores), 2),
            "success_rate": round(success_count / len(results), 2),
            "num_tasks": len(results)
        })

    return summary
