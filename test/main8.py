# 导入openai库
from openai import OpenAI


class LLM:
    def __init__(self, config):
        self.client = OpenAI(api_key=config.get("api_key"), base_url=config.get("url"))
        self.model_name = config.get("model_name")
        self.api_key = config.get("api_key")
        self.url = config.get("url")
        self.client = OpenAI(api_key=self.api_key, base_url=self.url)

    def generate_response(self, dialogue):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=dialogue,
        )
        return response.choices[0].message.content


def run():
    prompt = "你好"
    config = {
        "model_name": "GLM-4-Flash",
        "api_key": "9ecd9197579743c28f33512a4d83b66e.sB0PHkURnSgMt9ad",
        "url": "https://open.bigmodel.cn/api/paas/v4"
    }
    llm = LLM(config)

    dialogue = [
        {"role": "system", "content": "调皮一点回答"},
        {"role": "user", "content": "你好"},
    ]

    resource = llm.generate_response(dialogue)

    print(resource)

    print("--------------------")


if __name__ == "__main__":
    run()
