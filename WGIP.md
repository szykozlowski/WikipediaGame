##### Szymon Kozlowski

## Overview

Currently, the breadth first search algorithm we are using to find a path between two wikipedia links is rather slow.  This is because the algorithm adds/visits a large amount of pages, most of which are unnecesarry due to their irrelevence to the target of the search.

## Goal

My goal will be to create an algorithm that finds a path from the initial page to the target page in the shortest amount of time.  This won't find the *optimal* path as quickly as possible, just *a* path as quickly as possible.

## Suggested Improvement

Rather than using a breadth first search algorithm, I plan on utilizing a depth first search algorithm.  This should allow my program to quickly drill towards the intended target.  To do this, I plan on using a modification of the aStar pathfinding algorithm, which will utilize the python spaCy library for its heuristics.  This will evaluate each page's perceived distance from the target page, and proceed from there.  I'll keep a list of nodes that have been visited, along with their similarity score to the target.  I'll pursue the node that is most similar to the target, and add ta couple of the most similar links from that page to the search.

## Pseudocode

    while(set of nodes):
        current = node with highest similarity

        if(link in current page == goal)
            return
        
        sort(links in current page)
        for(i in range(couple most similar links))
            add(link,neighbors)

        for(neighbor of current):
            similarityScore = similarityScore(neighbor,target)
            if(similarityScore > max(bestSimilarity,similarityScore)
                this node is the current best path to pursue
                add(link,set)

## Milestones

    1.) 3/27/2024 Familiarize myself with, and pick a library that is capable of identyfiying the similarity score between words/phrases

    2.) 4/3/2024  Use the library to create a list of certain words and their similarity scores, and research whether this would be helpful in identifying links to pursue in the code

    3.) 4/7/2024 Create a version of the aStar algorithm without word similarity recognition that is capable of traversing from the start page to the finish page

    4.) 4/12/2024 Implement word similarity recognition into the aStar algorithm, and compare the results to the version without word similarity

    5.) 4/12/2024 From here, there will be two ways of proceeding that I can't identify until step 4.  Either the word similarity recognition library will significantly speed up the algorithm, or it won't.  If it does, 
        I'll explore other avenues of improving the effieciency of the algorithm.  If it doesn't, it's back to the drawing board.

## Progress

I've started researching the spaCy library to see if it will be useful for determining similarity between Wikipedia links.  I've created a basic script (located in spacytest.py) that takes a long list of words, and outputs their similarity scores.  I'll be testing some wikipedia pages, and seeing if the library will be useful.