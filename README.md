# About
COVID-19 has changed the world in terms of the way we live and work. The impact to populations and individuals cannot be overstated.
To better understand the public reactions to COVID-19 and their concerns, we will crowdsource tweets for early signals of public concerns (e.g. symptoms, needs) and topics of discussion (e.g. are masks useful or not). 
Understanding their concerns will help policymakers formulate effective communication channels to reach out to the public especially in addressing their most pressing concerns, and also understand the social impact of the policies enacted. 

# What this repo does (so far)
1. Collect tweets via Twitter Streaming API or Search API into AWS DynamoDB (tweetstream_dynamo.py) or .txt (tweetstream_txt.py) or .pkl
2. Reads tweets and metadata into pyspark or pandas dataframes (readtweets.py).
3. Preprocess tweet text (extended up to 280 char): tokenize, remove stop words and duplicates, normalize terms, 
 hashtags, mentions, emoticons (text_preprocess.py)
3. Topic modeling with Dynamic LDA (fit_lda.py)

# Other ideas to try (not done here)
Epidemiology has always thrived on big data. Even back in the 1840s, [John Snow](https://en.wikipedia.org/wiki/John_Snow), the father of Epidemiology, cleverly collected addresses from the local water utility provider and created the first outbreak dot map which located the Cholera epicenter to be the water pump on Broad St in London.

Today, we have even more data and methods available. This [figure](http://doi.org/10.1098/rstb.2018.0276) is a good way to see how they may all come together. With advances in deep sequential models, graph networks, stochastic agent-based modeling, etc, we can get really inventive!
![Outbreak epidemiology methods](https://royalsocietypublishing.org/cms/asset/7a1b3117-3a4c-4fda-a837-720ded4f8a84/rstb20180276f02.jpg)

# Other related repos
- [Risk factors from line list data](https://github.com/yenlow/nCoV2019)
- [SMMT](https://github.com/yenlow/SMMT)
- [Contribute](https://github.com/yenlow/nCoV2019/wiki/Data-and-code-suggestions) code and ideas!

Contact [Yen Low](https://www.linkedin.com/in/yenlow/) to join or [contribute](https://github.com/yenlow/nCoV2019/wiki/Data-and-code-suggestions) code and ideas here in the [Wiki](https://github.com/yenlow/nCoV2019/wiki/Data-and-code-suggestions) or [Issues](https://github.com/yenlow/nCoV2019/issues)!

