from openai import OpenAI

client = OpenAI(
    api_key=" API KEY "
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