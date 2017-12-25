# markovHHGG

Using a markov chain to try and generate a chapter of the Hitchhikers guide to the galaxy.

This program is a slightly better version of my previous markov chain experiments. 
It should be more efficient as it doesn't brute force the markov matrix, only generating rows and columns for transitions that exist in the corpus.
It also uses cPickle (faster implementation of pickle) to save the MarkovChain object after generation. Should you wish to ues a previously generated one.
