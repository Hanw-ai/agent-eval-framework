def simple_agent(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if "fibonacci" in prompt_lower:
        return """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
"""

    if "sql" in prompt_lower or "top 5 customers" in prompt_lower:
        return """
SELECT customer_id,
       SUM(purchase_amount) AS total_amount
FROM purchases
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 5;
"""

    if "division" in prompt_lower or "zero" in prompt_lower:
        return """
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
"""

    return ""
