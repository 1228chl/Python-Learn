from milvus_model.hybrid import BGEM3EmbeddingFunction


m3_path = "../rag_qa/models/bge-m3"
embedding_function = BGEM3EmbeddingFunction(model_name_or_path=m3_path, use_fp16=False, device='cpu')