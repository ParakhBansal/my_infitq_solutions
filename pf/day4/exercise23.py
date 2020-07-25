#PF-Exer-23
def translate(bilingual_dict,english_words_list):
    #Write your logic here
    swedish_words_list=[None]*len(english_words_list)
    for key in bilingual_dict:
        if key in english_words_list:
            ini=english_words_list.index(key)
            swedish_words_list[ini]=bilingual_dict[key]
    
        

    return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
