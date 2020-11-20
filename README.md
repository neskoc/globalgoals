# UN's 17 Sustainable Develpment Goals
Machine Learning project for predicting the "compliance" of Swedish research projects in regard to UN Sustainable Development Goals

Course: __DV2594 H20 lp12 Machine Learning for Streaming Data, Blekinge Institute of Technology__

## Project goals
Predict how well Swedish research projects are meeting the UN's Sustainable Development Goals ([17 Global Goals](https://www.globalamalen.se/)) by analaysing the historical research applications from [SweCRIS](https://www.swecris.se/) and match them with the UN's global goals (in Swedish: Globala målen)

## Project boundaries

1. Language of the documents (for analysis): Swedish
2. Document set: Application submission abstracts
3. In the first phase collected data from webb about global goals will be used as base for classifying and prediction
4. Tagged data provided by [Formas](https://formas.se/) will be used to evaluate model
5. The second phase
    - synonyms of the word identified in the first phase will be considered
    - Tagged data prom Formas will be used to expand the vocabulary (after some text analysis and processing)

> If you want to know more about the technical implementation check Code.md file.
