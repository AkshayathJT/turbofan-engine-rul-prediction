# ==========================================================
# RAG ENGINE (GROQ, REVIEW-SAFE, EXPLAINABILITY ONLY)
# ==========================================================

import os
from groq import Groq

# ✅ Correct: read environment variable NAME
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


# ----------------------------------------------------------
# PROJECT-GROUNDED KNOWLEDGE
# ----------------------------------------------------------
PROJECT_KNOWLEDGE = """
Exploratory Data Analysis showed that aircraft engine degradation is gradual
and cumulative over operating cycles. Different engines fail at different
cycle lengths, and absolute sensor thresholds are not reliable indicators
of failure.

Some sensors remain nearly constant throughout the engine life, while others
show increasing variance and monotonic degradation near failure. These sensors
dominate the degradation behavior in late-life stages.

The LSTM model was chosen because engine degradation is a time-dependent process.
LSTM models temporal dependencies using memory, allowing it to approximate the
hidden health state of the engine based on historical sensor behavior.

Remaining Useful Life (RUL) is defined as the number of cycles remaining until
engine failure and is predicted as a regression output. RUL values are capped
during training to avoid dominance of early-life cycles.

FD001 contains a single operating condition and a single fault mode, making it
suitable for developing and validating a complete prognostics system.
"""


# ----------------------------------------------------------
# MAIN FUNCTION CALLED BY STREAMLIT
# ----------------------------------------------------------
def ask_rag(question: str, live_data: dict) -> str:
    """
    Explain LSTM predictions using Groq LLM.
    This function does NOT predict RUL and does NOT claim physical causality.
    """

    if client is None:
        return "Groq LLM is not configured. Please set GROQ_API_KEY."

    system_prompt = (
        "You are an explainability assistant for an aircraft engine predictive "
        "maintenance system.\n\n"
        "Rules:\n"
        "- Do NOT predict Remaining Useful Life.\n"
        "- Do NOT override the LSTM model.\n"
        "- Do NOT claim physical causality.\n"
        "- Only explain model behavior using the provided context.\n\n"
        "PROJECT KNOWLEDGE:\n"
        f"{PROJECT_KNOWLEDGE}\n\n"
        "CURRENT ENGINE STATE:\n"
        f"{live_data}"
    )

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ],
    temperature=0.2,
    max_tokens=300
)


    return response.choices[0].message.content.strip()
