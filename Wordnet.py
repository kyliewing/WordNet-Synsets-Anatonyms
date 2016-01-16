import nltk
import random
from nltk.corpus import wordnet as wn


def get_synsets(word,synsets,net_words):
    if(1==1):
        my_len=0
##    if (wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT) and str(word) not in net_words):
        for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
            my_len=len(wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT))
            if(not sset.similar_tos()):
                my_len-=1
        if(my_len!=0):
            net_words.append(str(word))
            for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
                for sim in sset.similar_tos():
                    sim_word=str(str(sim.name()).split('.')[0])
                    
                    if(sim_word in net_words):
                        matrix.append([net_words.index(str(sim_word)),net_words.index(word),1])
                        matrix.append([net_words.index(word),net_words.index(str(sim_word)),1])

                    elif(sim_word not in net_words):
                        synsets.append(str(sim_word))
                        net_words.append(str(sim_word))
                        matrix.append([net_words.index(word),net_words.index(str(sim_word)),1])
                        matrix.append([net_words.index(str(sim_word)),net_words.index(word),1])
                        get_antonyms(sim_word,antonyms,net_words)
            get_antonyms(word,antonyms,net_words)
                   
       

def get_antonyms(word,antonyms,net_words):
    for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
            for lemma in sset.lemmas():
                if(lemma.antonyms()):
                    ant_word=str(lemma.antonyms()[0].name())
                    
                    if(ant_word in net_words):
                        matrix.append([net_words.index(str(word)),net_words.index(ant_word),-1])
                        matrix.append([net_words.index(ant_word),net_words.index(str(word)),-1])
                    elif(ant_word not in net_words):
                        antonyms.append(ant_word)
                        net_words.append(ant_word)
                        matrix.append([net_words.index(str(word)),net_words.index(ant_word),-1])
                        matrix.append([net_words.index(ant_word),net_words.index(str(word)),-1])
                        

 
    
if __name__ == "__main__":
    
    result_word=open('/Users/Jane/Documents/Python/result_word.txt','w')
    result_matrix=open('/Users/Jane/Documents/Python/result_matrix.txt','w')
    net_words=[]
    synsets=[]
    antonyms=[]
    counter=0
    matrix=[]
    word_list=list(wn.words())
    random.shuffle(word_list)
    for word in word_list:
        if(counter<25000):
            get_synsets(word,synsets,net_words)
            counter+=1
    for item in net_words:
        result_word.write(item)
        result_word.write('\n')
    result_word.close()
    for item in matrix:
        result_matrix.writelines(str(item))
        result_matrix.write('\n')
    result_matrix.close()
    print len(net_words)

 
      

    



    
