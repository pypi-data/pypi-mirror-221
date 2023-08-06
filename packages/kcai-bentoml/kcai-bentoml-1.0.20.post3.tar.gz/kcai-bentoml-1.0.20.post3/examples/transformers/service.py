import bentoml
import torch

from bentoml.io import JSON, NumpyNdarray


proccessor_runner = bentoml.transformers.get("sentence_bert_tokenizer").to_runner()
model_runner = bentoml.transformers.get("sentence_bert_model").to_runner()

svc = bentoml.Service("sentence_bert", runners=[proccessor_runner, model_runner])


@svc.api(input=JSON(), output=NumpyNdarray())
async def get_embedding(inp):
    keywords = inp["keywords"]
    encoded_input = await proccessor_runner.async_run(keywords, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = await model_runner.async_run(**encoded_input)
    sentence_embeddings = _mean_pooling(model_output, encoded_input['attention_mask'])
    return sentence_embeddings.detach().numpy()


def _mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
