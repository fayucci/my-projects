# My way in to Data Science:

## [Similarity of Charles Darwin's books](https://github.com/fayucci/my-projects/blob/master/Similarity_Charles_Darwin's_books/Charles_Darwin's_books.ipynb)
Charles Darwin wrote a lot of books on a wide range of topics and in this project I found how closely related his books are to each other based on how similar the discussed topics are.
I  first tokenized the corpus, then reduced inflected words to their word stem using a stemming process, then created a bag-of-words models (BoW) of each of our texts and then determined which tokens were the most specific to a book used a tf-idf model (term frequency–inverse document frequency) and last for measuring how related a book is to others I used a cosine similarity and visualized the results of a distance matrix as a dendrogram. [Source: DataCamp]

## [The left way to die](https://github.com/fayucci/my-projects/blob/master/The_left_way_to_die/notebook_left_handed.ipynb)
A 1991 study reported that left-handed people die on average nine years earlier than right-handed people. Nine years! Could this really be true? 
In this notebook, I explored this phenomenon using age distribution data to see for reproduced a difference in average age at death purely from the changing rates of left-handedness over time, refuting the claim of early death for left-handers. This notebook uses pandas and Bayesian statistics to analyze the probability of being a certain age at death given that you are reported as left-handed or right-handed. This notebook uses two datasets: [death distribution data for the United States](https://www.cdc.gov/nchs/data/statab/vs00199_table310.pdf) from the year 1999 and rates of [left-handedness digitized](https://pubmed.ncbi.nlm.nih.gov/1528408/) from a figure in this 1992 paper by Gilbert and Wysocki. [Source: DataCamp]

## [A Network Analysis of Game of Thrones](https://github.com/fayucci/my-projects/blob/master/A_Network_Analysis_of_Game_of_Thrones/notebook_games_of_thrones.ipynb)
In this notebook, I analyzed the co-occurrence network of the characters in the Game of Thrones books. Here, two characters are considered to co-occur if their names appear in the vicinity of 15 words from one another in the books. [Source: DataCamp]

## [Mind the ingredients of your cosmetics](https://github.com/fayucci/my-projects/blob/master/Mind_the_ingredients_of_your_cosmetics/notebook_cosmetics.ipynb)
 In this notebook, I created a content-based recommendation system where the 'content' will be the chemical components of cosmetics. Specifically,I processed ingredient lists for 1472 cosmetics on Sephora via word embedding, then visualize ingredient similarity using a machine learning method called t-SNE and an interactive visualization library called Bokeh. [Source: Datacamp]
 
## [Analizing Twitter Data]()
Twitter is a rich source for any data scientist, in this opportunity I did a thorough analysis of trends in Twitter.
I learned about the  big waves of thoughts and moods around the world. I focused on topics that were trending worldwide (WW) and in the United States (US).
The good news is that Twitter has its own API to collect data (I did not do this in this notebook).
After exploring the data, I compared the two sets of trends(WW and US), and I found one common trend that looked interesting, #WeLoveTheEarth, I focused on the tweets containing this hashtag, using the text, user names and hashtags can be inferred they were referring to a song about loving the Earth. 
To measure a tweet's popularity I used the retweet count and favorite count fields and visualized them in a DataFrame.
Finally from the text of the tweets, I could see different languages, so I created a frequency distribution for the languages, we observed  that most of the tweets were in English, there were a lot of tweets in an unknown language ('und'), Polish, Italian and Spanish were the next most frequently used language. [Source: DataCamp]

 
## [Data Analysis in Baseball](https://github.com/fayucci/my-projects/blob/master/Data_Analysis_in_Baseball/notebook_baseball.ipynb)
Statcast is a high-speed, high-accuracy, automated tool developed to analyze player movements and athletic abilities in Major League Baseball (MLB), Statcast is a state-of-the-art tracking system that uses high-resolution cameras and radar equipment to measure the precise location and movement of baseballs and baseball players.
In this notebook, I wrangled, analyzed, and visualized Statcast data to compare Mr. Judge and another (extremely large) teammate of his. [Source: DataCamp]

## [Classification of ASL with Deep Learning](https://github.com/fayucci/my-projects/blob/master/Classification_of_ASL_with_Deep_Learning/notebook_asl.ipynb) 
In this notebook, I trained a convolutional neural network to classify images of American Sign Language (ASL) letters. After loading, examining, and preprocessing the data, I trained the network and test its performance. [Source: DataCamp]

## [Rediscovery of Handwashing](https://github.com/fayucci/my-projects/blob/master/Rediscovery_of_Handwashing/notebook_semmelweis.ipynb)
In this notebook, I reanalyzed the data that made Dr.Semmelweis discover the importance of handwashing. I started by looking at the data that made Dr.Semmelweis realize that something was wrong with the procedures at Vienna General Hospital. The alarming number of deaths. [Source: DataCamp]
 
## [Exploring 67 years of LEGO](https://github.com/fayucci/my-projects/blob/master/Exploring_67_years_of_LEGO/notebook_lego.ipynb)
In this project, analyzed a dataset on every single lego block that has ever been built! A comprehensive database of lego blocks is provided by [Rebrickable](https://rebrickable.com/downloads/). Lego blocks offer an unlimited amount of fun across ages. I explored some interesting trends around colors, parts, and themes. [Source: DataCamp]
 
 ## [Exploring the Bitcoin Cryptocurrency Market](https://github.com/fayucci/my-projects/blob/master/Exploring_the_Bitcoin_Cryptocurrency_Market/notebook_bitcoins.ipynb)
In this project, I analyze the data of Bitcoin, Cryptocurrencies. Since the launch of Bitcoin in 2008, hundreds of similar projects based on the blockchain technology have emerged. We call these cryptocurrencies (also coins or cryptos in the Internet slang). [Source: DataCamp]
 
 ## [Generating Keywords for Google Ads](https://github.com/fayucci/my-projects/blob/maste/Generating_Keywords_for_Google_Ads/notebook_ads.ipynb)
Imagine working for a digital marketing agency, and the agency is approached by a massive online retailer of furniture. They want to test our skills at creating large campaigns for all of their website. We are tasked with creating a prototype set of keywords for search campaigns for their sofas section. The client says that they want us to generate keywords for the following products: sofas, convertible sofas, love seats, recliners, sofa beds.
The client is generally a low-cost retailer, offering many promotions and discounts. We will need to focus on such keywords. We will also need to move away from luxury keywords and topics, as we are targeting price-sensitive customers. [Source: DataCamp]

 
 ## [Find the users focus](https://github.com/fayucci/my-projects/blob/master/Find_the_users_focus/mouse_streamplot.ipynb)
 In this notebook analized the use case for bivariate kernel density estimate in web analytics by gathering the mouse movements of few users we are able to determine where are the users moving their cursors. To display the heatmap of the cusor location we overlap the bivariate kernel density estimate plot with a screenshot of the studies web page. The data set is simulated.

 
 ## [The GitHub History of Scala](https://github.com/fayucci/my-projects/blob/master/The_GitHub_History_of_Scala/notebook_scale.ipynb)
 In this notebook, read in, clean up, and visualize the real world project repository of Scala that spans data from a version control. [Source: DataCamp]
 
 ## [Exploring the Super Bowl](https://github.com/fayucci/my-projects/blob/master/Exploring_the_Super_Bowl/notebook_super_bowl.ipynb)
In this notebook, I found out how some of the elements of this show (Super Bowl) interact with each other. After exploring and cleaning the data a little, I'm going to answer questions like: What are the most extreme game outcomes?, How does the game affect television viewership? How have viewership, TV ratings, and ad cost evolved over time? and Who are the most prolific musicians in terms of halftime show performances? [Source: DataCamp]
 
 ## [The most use word in Moby Dick](https://github.com/fayucci/my-projects/blob/master/The_most_use_word_in_Moby_Dick/notebook_moby_dick.ipynb)
 What are the most frequent words in Herman Melville's novel Moby Dick and how often do they occur?
In this notebook, scraped the novel Moby Dick from the website [Project Gutenberg](https://www.gutenberg.org/) using the Python package requests. Then we'll extract words from this web data using BeautifulSoup. Finally, we'll dive into analyzing the distribution of words using the Natural Language ToolKit (nltk).[Source: DataCamp] 
