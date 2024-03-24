from langchain_community.chat_models.openai import ChatOpenAI


def build_llm(chat_args):
    return ChatOpenAI()
