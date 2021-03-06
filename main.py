import torch
import gluonnlp as nlp

from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel

from utils.classifier import BERTClassifier
from utils.predict import BERTpredict
    
if __name__ == '__main__':
    device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

    tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
    tok = tokenizer.tokenize
    bertmodel = BertModel.from_pretrained('skt/kobert-base-v1', return_dict=False)
    vocab = nlp.vocab.BERTVocab.from_sentencepiece(tokenizer.vocab_file, padding_token='[PAD]')

    ## Setting parameters
    max_len = 64
    batch_size = 64

    model = BERTClassifier(bertmodel,  dr_rate=0.5).to(device)
    model.load_state_dict(torch.load('./my_path/model8.pth',map_location=device))
    
    model_predict = BERTpredict(model,tok,vocab,max_len,batch_size,device)
    emotion = {0:'행복',1:'분노',2:'혐오',3:'공포',4:'중립',5:'슬픔',6:'놀람'}
    
    while True :
        sentence = input("하고싶은 말을 입력해주세요 : ")
        temp=[]
        if sentence == '0' :
            break
        temp = model_predict.predict(sentence)
        for i in range(7):
            print(emotion[i]+': '+str(temp[i])+'%')
        print("분석 감정: "+emotion[temp[7]])