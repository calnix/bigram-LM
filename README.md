# bigram-LM
Bigram Language Model (pwd cracking)

## **Background**:

Randomness after all does not come naturally to humans as a component of our thought process. To that end, password generators are offered as a solution. 
They purport a higher degree of randomness and look to alleviate the cognitive burden places on users, having to conjure a new password each time.

## **Objective**:

Examine the password strength of password generators.
Are they more predictable than one anticipates - is there some kind of underlying deterministic structure in the generation process?

## **Approach**:

We will attempt to find that structure, should it exist, using a probabilistic model. 

## **N-gram Language Model:**

A language model learns to predict the probability of a sequence of words or characters. 
Language models have the ability to model the rules of a language as a probability and are used effectively at a number of NLP related tasks like speech recognition and machine translation.
For our probabilistic modelling, we will use a character-level Bigram Language model. 

## **Password Generators (Data Collection) :**

1. Dashlane
2. Avast
3. passwordsgenerator.net
4. Lastpass
5. Roboform
6. Zoho

> we also use rockyou.txt, a common password dump comprises of over 14 million passwords, for model validation.

## **Password Strength:**

# rockyou.txt

![image](https://user-images.githubusercontent.com/22549197/160108901-77e259c0-d439-46c0-b319-aa55e11831fa.png)

To validate our model, we will apply it over a common password dump, rockyou.txt - comprising of 14,344,391 passwords.
Number of guesses the model could make was restricted to 100,000 and 1,000,000 tries. 
To mimic the sizes of samples we collected for each generator, we will constrict the size of training corpus to 5,000 and 10,000 respectively. 

The results above speak to the efficacy of the model; on the most constrained set of inputs of 5000 sized training corpus and 100,000 tries for guesses it was able to make 5,535 correct guesses – which is more that the training corpus size. We expect this to bode well for smaller sampling sizes.

The last two rows reflect the proportion split of 80% training and 20% test corpus as we plan to implement with the passwords generated from each password manager. 


# Password Generators

For each of the password generators, we will merge all the individual files into a combined larger corpus and randomly shuffle the elements before conducting the split between training and test corpus. 
This approach should allow the model to pick up deterministic characteristics if they are significantly present.

![image](https://user-images.githubusercontent.com/22549197/160109874-947bea54-5427-4216-9a4d-a2ca2d50f9ec.png)

The model was unable to make any correct guesses in any of the password generator corpus. 
Given these password managers use pseudo-random algorithms to generate their passwords, this is not that surprising. 

To offer a sense of this model’s efficacy, let us consider an eight-character password formulated from a universe of 26 upper-case letters, 26 lower-case letters, 10 digits and 18 symbols. 
This constitutes a total of 80 possible characters to choose from. For a random password, there are 80 possibilities for each character. 
Which means an eight-character password has 80^8 possibilities (1,677,721,600,000,000), over a quadrillion.

To combat the possibility that our test corpus might be a constrain due to its size, we repeated the experiment utilising a 20/80 split, in the way of training and test corpus respectively. 

![image](https://user-images.githubusercontent.com/22549197/160110176-64b6699d-79a6-4d41-ad29-7818f5a58284.png)


## **Limitations and Extensibility:**

An immediate and obvious limitation is the sample size for each type of password generator. Perhaps with a larger sample size and a larger number of allowed guesses, some correct guesses of the test corpus could have been made. 

We should consider the nature of randomness. 
While the model’s generated guesses did not occur within our test corpus, it could very be possible that at some point they very well might have as per the infinite monkey theorem. 

A problem with n-gram language models is that if we increase the n in n-grams it becomes computation-intensive. If we decrease the n, then long-term dependencies are not taken into consideration. 

Furthermore, there are newer approaches in language modelling that have had significant breakthroughs like GPT-3 which are worth exploring.

