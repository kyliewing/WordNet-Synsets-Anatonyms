import nltk
import random
from nltk.corpus import wordnet as wn


def get_synonyms(word,synonyms,net_words,origin_words):
        sim_counter=0
        for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
            for sim in sset.similar_tos():
                sim_counter+=1
        if(sim_counter!=0 and word not in synonyms):
            net_words.append(word)
            synonyms.append(word)
            origin_words.append(word)
        for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
            for sim in sset.similar_tos():
                sim_word=str(str(sim.name()).split('.')[0])
                if(sim_word not in synonyms):
                    net_words.append(sim_word)
                    synonyms.append(sim_word)


def get_antonyms(antonyms,synonyms):
    for word in synonyms:
        for sset in wn.synsets(word,pos=wn.ADJ or wn.ADJ_SAT):
            for lemma in sset.lemmas():
                if(lemma.antonyms()):
                    ant_word=str(lemma.antonyms()[0].name())
                    if(ant_word not in net_words):
                        net_words.append(ant_word)
                        antonyms.append(ant_word)
         

def build_matrix(length,net_words):
    result_matrix=open('/Users/Jane/Documents/Python/result_matrix.txt','w')
    matrix=[[0 for col in range(length)] for row in range(length)]
##    for i in range(length):
##        for j in range(length):
##            for sset in wn.synsets(net_words[i],pos=wn.ADJ or wn.ADJ_SAT):
##                for sim in sset.similar_tos():
##                    if(net_words[j]==str(str(sim.name()).split('.')[0])):
##                        matrix[i][j]=1
##                        matrix[j][i]=1
##                for lemma in sset.lemmas():
##                    if(lemma.antonyms()):
##                        if(net_words[j]==str(lemma.antonyms()[0].name())):
##                            matrix[i][j]=-1
##                            matrix[j][i]=-1
    for element in range(length):
        element_synonyms=[]
        element_antonyms=[]
        for sset in wn.synsets(net_words[element],pos=wn.ADJ or wn.ADJ_SAT):
            for sim in sset.similar_tos():
                element_synonyms.append(str(str(sim.name()).split('.')[0]))
            for lemma in sset.lemmas():
                if(lemma.antonyms()):
                    element_antonyms.append(str(lemma.antonyms()[0].name()))
        inter_synonyms=list(set(element_synonyms).intersection(set(net_words)))
        inter_antonyms=list(set(element_antonyms).intersection(set(net_words)))
        for item in inter_synonyms:
            matrix[element][net_words.index(item)]=1
            matrix[net_words.index(item)][element]=1
        for item in inter_antonyms:
            matrix[element][net_words.index(item)]=-1
            matrix[net_words.index(item)][element]=-1
        
    for i in range(len(net_words)):
        for j in range(len(net_words)):
            if(matrix[i][j]!=0 and i!=j):
                result_matrix.write("%d%s%d%s%d%s"%(i,',',j,',',matrix[i][j],'\n'))
    result_matrix.close()
    return matrix
    

    
if __name__ == "__main__":
    
    result_word=open('/Users/Jane/Documents/Python/result_word.txt','w')
    net_words=[]
    synonyms=[]
    origin_synonyms=[]
    antonyms=[]
    origin_words=[]
    iterations=2
    
    word_list=list(wn.words())
    random.shuffle(word_list)
    for word in word_list:
        if(len(origin_words)<400):
            get_synonyms(word,synonyms,net_words,origin_words)
    
    for inter in range(iterations-1):
        temp_synonyms=synonyms
        for i in range(len(temp_synonyms)):
            get_synonyms(temp_synonyms[i],synonyms,net_words,origin_words)
    get_antonyms(antonyms,synonyms)
    print 'stage3'
    for item in net_words:
        result_word.write(item)
        result_word.write('\n')
    result_word.close()
    my_matrix=build_matrix(len(net_words),net_words)
    print 'stage4'
    print len(synonyms)#,synonyms
    print len(antonyms)#,antonyms
    print len(net_words)#,net_words

    
                

