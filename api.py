from huggingface_hub import InferenceClient

def ner(text):

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )

    result = client.token_classification(text, model="Davlan/xlm-roberta-base-ner-hrl")
    return [(i.word, i.entity_group) for i in result]