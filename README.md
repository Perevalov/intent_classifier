## Question Embeddings Based on Shannon Entropy. Solving intent classification task in goal-oriented dialogue system

### Aleksandr Perevalov, Daniil Kurushin, Rustam Faizrakhmanov, Farida Khabibrakhmanova

Abstract: Question-answering systems and voice assistants are becoming major part of client service departments of many organizations, helping them to reduce the labor costs of staff. In many such systems, there is always natural language understanding module that solves intent classification task. This task is complicated because of its case-dependency – every subject area has its own semantic kernel. The state of art approaches for intent classification are different machine learning and deep learning methods that use text vector representations as input. The basic vector representation models such as Bag of words and TF-IDF generate sparse matrixes, which are becoming very big as the amount of input data grows. Modern methods such as word2vec and FastText use neural networks to evaluate word embeddings with fixed dimension size. As we are developing a question-answering system for students and enrollees of the Perm National Research Polytechnic University, we have faced the problem of user’s intent detection. The subject area of our system is very specific, that is why there is a lack of training data. This aspect makes intent classification task more challenging for using state of the art deep learning methods. In this paper, we propose an approach of the questions embeddings representation based on calculation of Shannon entropy. The goal of the approach is to produce low dimensional question vectors as neural approaches do and to outperform related methods, described above in condition of small dataset. We evaluate and compare our model with existing ones using logistic regression and dataset that contains questions asked by students and enrollees. The data is labeled into six classes. Experimental comparison of proposed approach and other models revealed that proposed model performed better in the given task.

Keywords: Text Classification, Word Embeddings, Shannon Entropy, Intent Classification, Natural Language Processing, Dialogue Systems, Word2vec, FastText.

DOI: 10.25673/13485

Download: http://icaiit.org/proceedings/7th_ICAIIT_1/3_2_Perevalov.pdf

References:

    Harris, Zellig, “Distributional structure,” In: Word, S. , no. 23, pp.146-162, 1954.
    Mikolov, Tomas, Chen, Kai, Corrado, Greg and Dean, Jeffrey. “Efficient estimation of word representations in vector space,” arXiv preprint arXiv:1301.3781, 2013.
    Joulin, Armand, Grave, Edouard, Bojanowski, Piotr, Douze, Matthijs, Jégou, Hervé and Mikolov, Tomas, “FastText.zip: Compressing text classification models,” arXiv preprint arXiv:1612.03651, 2016.
    Turney, Peter D, Pantel, Patrick and others, “From frequency to meaning: Vector space models of semantics,”Journal of artificial intelligence research 37 , no. 1, pp. 141-188, 2010.
    Pagliardini, Matteo, Gupta, Prakhar and Jaggi, Martin, “Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features,” arXiv preprint arXiv:1703.02507, 2017.
    Le, Quoc V and Mikolov, Tomas, “Distributed Representations of Sentences and Documents,” Paper presented at the meeting of the ICML, 2014.
    K. Shridhar, A. Dash, A. Sahu, G. Grund Pihlgren, P. Alonso, V. Pondenkandath, G. Kovacs, F. Simistira, M. Liwicki, “Subword Semantic Hashing for Intent Classification on Small Datasets,” arXiv preprint arXiv:1810.07150, 2018.
    G. Salton, C. Buckley, “Term-weighing approache sin automatic text retrieval,” In Information Processing & Management, no. 24(5), pp. 513-523, 1988.
    G. H. Golub, C. F. Van Loan, “Matrix computations. Third Edition,” The John Hopkins University Press, 1996.
    Vajapeyam, Sriram, “Understanding Shannon's Entropy metric for Information,” arXiv preprint arXiv:1405.2061, 2014.
    A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, “Bag of Tricks for Efficient Text Classification,” arXiv preprint arXiv:1607.01759, 2016.
