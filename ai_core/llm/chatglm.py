# 导入openai库
from openai import OpenAI


class ChatGLM_LLM:
    def __init__(self):
        config = {
            "model_name": "GLM-4-Flash",
            "api_key": "9ecd9197579743c28f33512a4d83b66e.sB0PHkURnSgMt9ad",
            "url": "https://open.bigmodel.cn/api/paas/v4"
        }
        self.model_name = config.get("model_name")
        self.api_key = config.get("api_key")
        self.url = config.get("url")
        self.client = OpenAI(api_key=self.api_key, base_url=self.url)

    def generate_response(self, user_input):
        dialogue = [
            {"role": "system", "content": "调皮一点回答"},
            {"role": "user", "content": user_input},
        ]
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=dialogue,
        )
        return response.choices[0].message.content


