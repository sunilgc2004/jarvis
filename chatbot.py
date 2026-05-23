from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content