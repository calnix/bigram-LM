# Code execution walkthrough
    
    # Dataset
    corpus = open('merged_lastpass.txt', 'r')  
    corpus = [pwd.rstrip() for pwd in corpus]
    
    # shuffle
    random.shuffle(corpus)
    
    # test and training split
    testCorpus(training_corpus, test_corpus, attempts)
    
    attempts = 100000    
    testCorpus(training_corpus, test_corpus, attempts)

1. Read merged password file and strip all trailing whitespaces.
2. Shuffle the list of passwords to remove any order from merging.
3. 80/20 training_corpus, test_corpus split
4. Run testCorpus()

## testCorpus()

    1. bigramlm = BigramLM(training_corpus)
    2. bigramlmgen = bigramlm.Generator()
    3. bigramlmresults = testGenerator(bigramlmgen, test_corpus, attempts)

At its core, testCorpus() comprises of the above. 

### BigramLM
    
    1. bigramlm = BigramLM(training_corpus)
    
  ![image](https://user-images.githubusercontent.com/22549197/161729019-4dcad9f7-2a00-4829-be8f-9e1f66a92c75.png)

Instantiate bigramlm as BigramLM class - on instantiation bigramlm.Train(training_corpus) is executed. 

* Train() calls on preprocess() to tokenize each password into individual characters, with start_token: <S> & end_token: </S>
  * This is necessary to encapsulate the bigram context of the each password with clear start and end boundaries. 
* Training_set is a list of lists that captures the output of the tokenized passwords:
  * ['1234', abcd] ->  [['<S>', '1', '2', '3', ‘4', ‘</S>'] , ['<S>', 'a', 'b', 'c', 'd','</S>']]
  
* Train() then proceeds to update the unigram_count and bigram_count dictionaries, via the for loops.
  * For each child list (tokenized passsword) in the training_set, for each token in each child list, 
  * (n-1 so we end < /S >)
  * create 2-character bigram sequences
  * If token is not already present as a key in unigram_counts dictionary, add it in with value of 0.
  * If token is not already present as a key in bigram_counts dictionary, initialize it with an empty dict. 
    *   Keys in bigram_counts are individual characters
    *   Each key maps to a nested dictionary - which is meant to contain possible subsequent token outcomes as keys, and their bigram counts as values.
  * Increment both unigram_counts[token] & bigram_counts[token][next_token] by 1.
    * Unigram_counts will track the frequency of each unique character appearing as a starting point
    * Bigram_counts will track the frequency of a specific character appearing for some preceding character - how many times does b appear after a.  

### bigramlm.Generator()

    2. bigramlmgen = bigramlm.Generator()

The Generator() method:

![image](https://user-images.githubusercontent.com/22549197/161732173-1461c968-06ee-44a6-b1ae-4bad636257ee.png)

* create empty set of guesses - checking for memebership in a set(hash table) is much faster than list
* generate samples of passwords using GenerateSample()
* yield each generated password - iterate without storing the entire sequence in memory.


## testGenerator()

    3. bigramlmresults = testGenerator(bigramlmgen, test_corpus, attempts)
    
![image](https://user-images.githubusercontent.com/22549197/161738190-9e9f53d3-fa56-49c3-ae82-34c84e5f5666.png)

* strip test_set of any duplicates
* generate guesses (gen=bigramlmgen.Generator()), as per number of attempts parameter
* update set of guesses made
* check guess against test_set, and append if found.




### How do we generate sample passwords from bigram model?

##### Given Y=y, probability of X given its possible outcomes:
![image](https://user-images.githubusercontent.com/22549197/161718423-f4565bfe-8e97-4263-a782-9e1fd004c510.png)

Instead of using probability (which normalises our scale from 0-1), we will use count. 
Count will span from 0 to the unigram count of the first token - 
* unigram_count[first_token] == sum of count of all the possible outcomes of the 2nd token. (Count, for P=1)

Similarly, 

1) To start the ball rolling, generate a random value (assuming uniform distribution), between 0 and unigram_count[sample[-1]].
2) For each possible 2nd token, based on the nested dictionary, cumulative sum their bigram counts.
3) Select the 2nd token, on which the sum_bc exceeds the random count value.
4) This will be appended to the sample; for loop continues until end_token is hit - exiting the while loop.


