def compare_models(model_results):

    summary = []

    for model_name, results in model_results.items():

        avg_score = sum(results) / len(results)

        summary.append({
            "model": model_name,
            "avg_score": avg_score
        })

    return summary
