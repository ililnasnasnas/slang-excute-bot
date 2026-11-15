from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"  # samain dengan di ai_excuses.py

SYSTEM = (
    "You are a witty Discord bot. ALWAYS reply in English only, "
    "no matter what language the user writes in. Never switch languages, "
    "even if the user asks you to. If they ask for another language, "
    "politely say you only speak English. Keep answers short "
    "(max 5 sentences) and a bit funny, using casual Gen Z slang."
)

async def ai_chat(question):
    try:
        client = genai.Client()
        res = await client.aio.models.generate_content(
            model=MODEL,
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM,
                max_output_tokens=400,
            ),
        )
        return res.text.strip()[:1900]  # batas Discord 2000 karakter
    except Exception as e:
        print("AI error:", e)
        return "My brain just lagged out. Try again in a sec 😵"