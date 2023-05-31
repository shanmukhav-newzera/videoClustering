# from transformers import AutoTokenizer, AutoModel, util
# import torch
# import torch.nn.functional as F

# #Mean Pooling - Take attention mask into account for correct averaging
# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0] #First element of model_output contains all token embeddings
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# # Sentences we want sentence embeddings for
# sentences = ['This is an example sentence', 'Each sentence is converted']

# # Load model from HuggingFace Hub
# tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
# model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

# # Tokenize sentences
# encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# # Compute token embeddings
# with torch.no_grad():
#     model_output = model(**encoded_input)

# # Perform pooling
# sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

# # Normalize embeddings
# sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

# print("Sentence embeddings:")
# print(sentence_embeddings)

from sentence_transformers import SentenceTransformer, util
sentences = ["Texting random numbers. These random numbers keep texting me. It's getting so annoying. Um You're a random number that's texting me right now. I'm not random. I'm a cool guy. The only random thing I do is text random numbers. So you are random then. No, you're the random. I'm the one who started this conversation. But me receiving the text means that you are a random number to me. I guess everyone has their opinions. Some people don't enjoy prison. I did. Why did you go to prison? Oh, I scammed random people through text. I was making thousands of dollars a month. Stupid laws, man. Are you gonna try and scam me? Well, your car warranty has expired. Uh, please tap the follow button for more.", "I am sad"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Compute embedding for both lists
embedding_1= model.encode(sentences[0], convert_to_tensor=True)
embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

print(util.pytorch_cos_sim(embedding_1, embedding_2))
## tensor([[0.6003]])
