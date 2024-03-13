##### Szymon Kozlowski

## Overview

Currently, the breadth first search algorithm we are using to find a path between two wikipedia links is rather slow.  This is because the algorithm adds/visits a large amount of pages, most of which are unnecesarry due to their irrelevence to the target of the search.

## Goal

My goal will be to create an algorithm that finds a path from the initial page to the target page in the shortest amount of time.  This won't find the *optimal* path as quickly as possible, just *a* path as quickly as possible.

## Suggested Improvement

Rather than using a breadth first search algorithm, I plan on utilizing a depth first search algorithm.  This should allow my program to quickly drill towards the intended target.  To do this, I plan on using a modification of the aStar pathfinding algorithm, which will utilize the python spaCy library for its heuristics.  This will evaluate each page's perceived distance from the target page, and proceed from there.

## Pseudocode

    while(set of nodes):
        current = node with highest similarity

        if(current == goal)
            return
        
        sort(links in current page)
        for(i in range(couple most similar links))
            add(link,set)

        for(neighbor of current):
            similarityScore = similarityScore(neighbor,target)
            if(similarityScore > max(bestSimilarity,similarityScore)
                this node is the current best path to pursue

