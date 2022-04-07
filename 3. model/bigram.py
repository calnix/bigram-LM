import random

start_token = "<S>"
end_token = "</S>"

#Tokenize input:  [['<S>', '1', '</S>'], ['<S>', '2', '</S>'], ['<S>', '3', '</S>'], ['<S>', '4', '</S>']]
def preprocess(corpus):
    return [[start_token] + [token for token in pwd] + [end_token] for pwd in corpus]

class BigramLM:
    def __init__(self, training_corpus):
        self.bigram_counts = {}  #dict
        self.unigram_counts = {}
        self.Train(training_corpus)

    def Train(self, training_corpus):
        training_set = preprocess(training_corpus)  #tokenize input into characters
        for pwd in training_set:
            for i in range(len(pwd)-1):
                token = pwd[i]
                next_token = pwd[i+1]
                if not token in self.unigram_counts:
                    self.unigram_counts[token] = 0   #bigramLM.unigram_counts['some_token'] = 0  - count from 0
                if not token in self.bigram_counts:
                    self.bigram_counts[token] = {}            #bigramLM.bigram_counts['some_token'] = {} - init first iteration as empty dict, nested.
                if not next_token in self.bigram_counts[token]:
                    self.bigram_counts[token][next_token] = 0  #nested dict
                self.unigram_counts[token] += 1
                self.bigram_counts[token][next_token] += 1

    def GenerateSample(self):
        sample = [start_token]
        while not sample[-1] == end_token:
            # random floating point number in range [0,unigram_counts[<S>,e1,e2,...,en])
            selector = random.uniform(0, self.unigram_counts[sample[-1]])
            sum_bc = 0
            for bigram in self.bigram_counts[sample[-1]]:
                sum_bc += self.bigram_counts[sample[-1]][bigram]
                if sum_bc > selector:
                    sample.append(bigram)
                    break
        return ''.join(sample[1:-1])

    def Generator(self):
        guesses = set()
        while True:
            pwd = self.GenerateSample()
            if not pwd in guesses:
                guesses.update([pwd])
                yield pwd



# how many pwds in test_corpus can generator guess
# bigramlm.Generator(),test_corpus,tries
def testGenerator(gen, test_corpus, attempts):
    found = 0
    x = []
    # set of unique pwds
    test_set = set(test_corpus)

    # set of unique guesses
    guesses = set()
    for i in range(attempts):
        # yield next iteration
        guess = next(gen)
        if not guess in guesses:
            # unique new guess
            guesses.update([guess])
            # check if guess is in test set
            if guess in test_set:
                # count of found guesses
                found += 1
                x.append(guess)


    return found, x


def testCorpus(training_corpus, test_corpus, attempts):
    print("First 5 training passwords: ", training_corpus[:5])
    print("Length of training_corpus:", len(training_corpus))

    print("First 5 test passwords: ", test_corpus[:5])
    print("Length of test_corpus:", len(test_corpus))

    bigramlm = BigramLM(training_corpus)
    bigramlmgen = bigramlm.Generator()
    bigramlmresults = testGenerator(bigramlmgen, test_corpus, attempts)

    print("Attempts: %d | Correct guesses: %d" % (attempts, bigramlmresults[0]))
    print("List of correct guesses:");
    print(bigramlmresults[1])

###################################################################################################

# Dataset
# corpus = open('rockyou.txt', 'r', encoding="utf8", errors='ignore')  #open read
corpus = open('merged_zoho.txt', 'r')  # open read
corpus = [pwd.rstrip() for pwd in corpus]

# shuffle
random.shuffle(corpus)

# test and training split
training_corpus = corpus[:int((len(corpus) + 1) * .80)]  # 80% to training set
test_corpus = corpus[int((len(corpus) + 1) * .80):]  # Splits 20% data to test set


# how many attempts
attempts = 100000        #100K
#attempts = 1000000        #1 MM

#capture testset
# execute
testCorpus(training_corpus, test_corpus, attempts)





