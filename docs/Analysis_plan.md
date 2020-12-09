# Topic mining: Test plan

The project is about topic mining where we have 17 classes of data s.k. UN global sustainability goals described in 17 documents (the "absolutely" correct classes).

1. We have the database with __24.241__ documents (submissions for the project funding) which need to be classified according to the 17 global goals.
2. Every application can belong to 0 or more classes (at most 3). So basically there are 17 main + 1 "other" topic
3. Documents are in Swedish language.
4. W have 3 types of tagged documents
    - (a.1) Approximately 800 manually tagged documents which cover 16 topics (there is no topic belonging to one particular class) + some not belonging to any. This is the most correct tagging because it was done by same person which is expert in the area
    - (a.2) Same documents are also tagged in 3 levels (1 main and 2 axillary class) by the applicants themselves though the quality is questionable
    - (b) There are approximately 15.000 more taggings which are the self-assessed classifications of the submissions made in at most 2 classes (number of documents are around 5-7.000). There was no evaluation of the quality of the classifications but the experience from the evaluation made for documents in a.1/a.2 leads to conclusion that quality is not that high especially for the axillary classifications

Complete data set is 24.241 "documents" (submissions).

So basically we have 3 classes of tagged documents.
1. __17__ documents which are most correct (1 per each topic)
2. above described as (a.1): __800__ documents in 16+1 topics, this tagging has high quality
    - (a.2) I think this classification should be skipped due to a.1 been more correct
3. above described as (b): __15.000__ taggings that are of questionable quality

The idea is to use weighting of the documents for training. Weights would be simulated by using several instances (repeating) of the same document in the training/test set where:
- (1) has multiplication coefficient MC (3 to 5)
- (a.1) has coefficient MCa = (2 to 3)
- (b) MCb = 1

It is unclear for now whether second and third level of classification should be considered at all.

Depending on the available the plan is to test and possible use the following 3 types of algorithms:
1. similarity, in this case similarity to only first group of documents (24:000 : 17)
2. Multinomial Naive Bayes
3. Neural networks

Compare the results and possibly use majority voting.
