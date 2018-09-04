murder_note = 'You may call me heartless, a killer, a monster, a murderer, but I\'m still NOTHING compared to the ' \
              'villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and ' \
              'feed Jay\'s massive, massive ego. SURE you think you know him! You\'ve seen him smiling for the ' \
              'cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was ' \
              'a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, ' \
              'like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things ' \
              'that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his ' \
              'words. I miss my former cast members, all of them very much. And we had to live with him, live in his ' \
              'home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN\'T ' \
              'REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was ' \
              'stick, he told us last night that we were all a terrible terrible disappointment and none of us would ' \
              'ever amount to anything, and that regardless of who won the contest he would never speak to any of us ' \
              'again! It\'s definitely the things like this you can feel in your gut how wrong he is! Well I showed ' \
              'him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn\'t going to ' \
              'be pushed around any longer, and I wasn\'t going to let him go on pretending that he was some saint ' \
              'when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to ' \
              'know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place ' \
              'without him.'

lily_trebuchet_intro = 'Hi, I\'m Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under ' \
                       'a warm blanket with a book. So they gave this little questionnaire to use for our bios so ' \
                       'lets get started. What are some of my least favorite household chores? Dishes, oh yes it\'s ' \
                       'definitely the dishes, I just hate doing them, don\'t you? Who is your favorite actor and ' \
                       'why? Hmm, that\'s a hard one, but I think recently I\'ll have to go with Michael B. Jordan, ' \
                       'every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can\'t ' \
                       'believe what he does for the cameras! Okay okay next question, what is your perfect date? ' \
                       'Well it starts with a nice dinner at a delicious but small restaurant, you know like one of ' \
                       'those places where the owner is in the back and comes out to talk to you and ask you how your ' \
                       'meal was. My favorite form of art? Another hard one, but I think I\'ll have to go with music, ' \
                       'music you can feel in your whole body and it is electrifying and best of all, you can dance ' \
                       'to it! Okay final question, let\'s see, What are three things you cannot live without? Well ' \
                       'first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is ' \
                       'pasta, definitely pasta, and the third I think is my family, I love all of them very much and ' \
                       'they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want ' \
                       'to be the first to walk down the aisle with him, but I think he might truly be the one for ' \
                       'me. Okay that\'s it for the bio, I hope you have fun watching the show! '

myrtle_beech_intro = 'Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, ' \
                     'thinking, and doing my taxes. I entered this competition because I want a serious relationship. ' \
                     'I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had ' \
                     'no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He ' \
                     'called it a "walk". A "walk" with no destination. Can you imagine? I like every action I take ' \
                     'to have a measurable effect. When I see a movie, I like to walk away with insights that I did ' \
                     'not have before. When I take a bike ride, there better be a worthy destination at the end of ' \
                     'the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief ' \
                     'that one does not make and keep money without having a modicum of discipline. As such, ' \
                     'I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. ' \
                     'Thank you for the opportunity to introduce myself. I look forward to the competition. '

gregg_t_fishy_intro = 'A most good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years ' \
                      'young, an adventurous spirit and I\'ve never lost my sense of childlike wonder. I do love to ' \
                      'be in the backyard gardening and I have the most extraordinary time when I\'m fishing. Fishing ' \
                      'for what, you might find yourself asking? Why, I happen to always be fishing for compliments ' \
                      'of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who ' \
                      'dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and ' \
                      'short walks through greenhouses. I hope that Jay will be as absolutely interesting as he ' \
                      'appears on the television, I find that he has some of the most curious tastes in style and ' \
                      'humor. When I\'m out and about I quite enjoy hearing tales that instill in my heart of hearts ' \
                      'the fascination that beguiles my every day life, every fiber of my being scintillates and ' \
                      'vascillates with extreme pleasure during one of these charming anecdotes and significantly ' \
                      'pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay ' \
                      'To Remember, it certainly seems like a grand time to explore life and love. '


def get_average_sentence_length(text):
    # First I made all sentence-ending punctuation a curly brace so I could use curly braces as delimiters. I also
    # removed apostrophes to ensure compound words
    delimited_sentences = text.replace('.', '}').replace('!', '}').replace('?', '}')#.replace("'", "")
    sentence_split = delimited_sentences.split('}')
    sentences_stripped = [sentence.strip() for sentence in sentence_split]
    # I wrote this section when I thought it was looking for the average number of characters in a sentence,
    # not the average number of words. I still think there's some value in this, since it accounts for word length, but
    # whatever. It's not necessary so I commented it out.
    ### characters_in_sentence = [len(sentence) for sentence in sentences_stripped]
    ### characters_in_sentence.pop()
    ### average_sentence_characters = round((sum(characters_in_sentence) / len(characters_in_sentence)), 2)
    words = []
    for lst in sentences_stripped:
        words.append(lst)
    # words_in_sentences was added because each of the samples included a blank string at the end, ''. This line removes
    # those blank strings.
    words_in_sentences = list(filter(None, words))
    # count_words is a list of integers corresponding to the number of words in each sentence.
    count_words = [len(sentence) for sentence in words_in_sentences]
    # average_words is the final result. I didn't need to make it a local variable and then return the local variable,
    # but it's easier to read this way I think.
    average_words = round((sum(count_words) / len(count_words)))
    return average_words


def prepare_text(text):
    delimited_sentences = text.replace('.', '').replace('!', '').replace('?', '').replace("'", "").replace(",", "")
    words = delimited_sentences.lower().split(' ')
    word_list = list(filter(None, words))
    return word_list


def build_frequency_table(corpus):
    # Step one is to build a dictionary with the words ask keys, and the number of times that word appears in the sample
    # as the values. If the word is in the dictionary already, this function adds 1 to the value associated with that
    # key. If it throws a KeyError, it creates a new key for that word and sets the value at 1.
    counter_dict = {}
    for word in corpus:
        try:
            counter_dict[word] += 1
        except KeyError:
            counter_dict[word] = 1
    return counter_dict
    # This next part sorts key:value pairs by value. I commented it out because isn't necessary for the equation,  it
    # was just helpful when I was testing the function.
    #sorter = [[k, counter_dict[k]] for k in sorted(counter_dict, key=counter_dict.get, reverse=True)]
    #frequency_count = {}
    #for item in sorter:
    #    frequency_count[item[0]] = item[1]
    #return frequency_count


def ngram_creator(text_list):
    ngrams = []
    for i in range(len(text_list) - 1):
        ngrams.append("{} {}".format(str(text_list[i]), str(text_list[i + 1])))
    return ngrams


class TextSample:

    similarity_score = None

    def __init__(self, text, author):
        self.raw_text = text
        self.author = author
        self.average_sentence_length = get_average_sentence_length(self.raw_text)
        self.word_list = prepare_text(self.raw_text)
        self.word_count_frequency = build_frequency_table(self.word_list)
        self.ngrams = ngram_creator(self.word_list)
        self.ngram_frequency = build_frequency_table(self.ngrams)

    def __repr__(self):
        return "{}'s writing sample has an average sentence length of {} words.".format(self.author, self.average_sentence_length)


murderer_sample = TextSample(murder_note, 'Murderer')
lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
gregg_sample = TextSample(gregg_t_fishy_intro, 'Gregg T. Fishy')


def frequency_comparison(table1, table2):
    appearances = {}
    mutual_appearances = {}
    for t1key in table1.keys():
        if t1key in table2:
            if table1[t1key] <= table2[t1key]:
                mutual_appearances[t1key] = table1[t1key]
                appearances[t1key] = table2[t1key]
            else:
                mutual_appearances[t1key] = table2[t1key]
                appearances[t1key] = table1[t1key]
        else:
            appearances[t1key] = table1[t1key]
    for t2key in table2.keys():
        if t2key not in appearances.keys():
            appearances[t2key] = table2[t2key]
    return sum(mutual_appearances.values())/(sum(mutual_appearances.values())+sum(appearances.values()))


def percent_difference(value1, value2):
    unit1 = abs(value1 - value2)
    unit2 = (value1 + value2)/2
    return unit1/unit2


def find_text_similarity(text_sample1, text_sample2):
    sentence_length_difference = abs(1 - percent_difference(text_sample2.average_sentence_length, text_sample1.average_sentence_length))
    word_count_similarity = frequency_comparison(text_sample1.word_count_frequency, text_sample2.word_count_frequency)
    ngram_similarity = frequency_comparison(text_sample1.ngram_frequency, text_sample2.ngram_frequency)
    total = (sentence_length_difference + word_count_similarity + ngram_similarity) / 3
    return total


lily_sample.similarity_score = find_text_similarity(murderer_sample, lily_sample)
myrtle_sample.similarity_score = find_text_similarity(murderer_sample, myrtle_sample)
gregg_sample.similarity_score = find_text_similarity(murderer_sample, gregg_sample)


def print_results(contestant):
    print("{AUTHOR}'s writing sample and the killer's note are {0:.2f}% alike.".format(contestant.similarity_score*100, AUTHOR=contestant.author))


contestants = [lily_sample, myrtle_sample, gregg_sample]

for person in contestants:
    print_results(person)


def who_dunnit(potential_killers):
    max_score = 0
    killer = None
    for pk in potential_killers:
        if pk.similarity_score > max_score:
            max_score = pk.similarity_score
            killer = pk.author
    return "The killer was {}!".format(killer).upper()

print()
print(who_dunnit(contestants))



