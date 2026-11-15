from google import genai
from google.genai import types
from core.excuses import make_excuse

MODEL = "gemini-3.5-flash-lite"

STYLE = {
    0: "believable but funny",
    1: "dramatic and exaggerated",
    2: "completely unhinged and absurd",
}

SYSTEM = (
    "You write funny excuses for being late, in Gen Z English slang. "
    "Reply with ONE excuse, max 2 sentences, no intro."
)

async def ai_excuse(user_id, chaos=1, situation=""):
    try:
        client = genai.Client()  # baca GEMINI_API_KEY otomatis
        res = await client.aio.models.generate_content(
            model=MODEL,
            contents=f"Style: {STYLE[chaos]}. Situation: {situation or 'late to something'}",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM,
                max_output_tokens=150,
            ),
        )
        return res.text.strip()
    except Exception as e:
        print("AI error:", e)
        return make_excuse(user_id, chaos)