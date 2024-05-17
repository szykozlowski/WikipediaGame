# Contributions

## Goal

To improve the initial code for the Wikipedia game, my goal was to create an algorithm that significantly sped up the sample code, and eliminated the length of path limitation. In this project,  I solely cared about the speed of the found path, and did not care for how long it ended up being.

## Methodology

My initial idea was to use sentiment analysis as a heuristic for an aStar algrithm to find a quick path to purse  However, I quickly realized that sentiment analysis in the wikipedia project would probably not lead to quicker times.  First, a multitude of wikipedia pages contain terms that are not found in many free to use sentiment analysis databases (usually proper nouns).  Second, running this analysis on hundreds of links was rather slow.  Instead, I decided to use a backtracking approach that utilized a popular wikipedia page as a midpoint.


### Search Algorithm

While a Breadth First Search will result in an optimal path, I chose to change it to a Depth First Search to find a path quickly.  This is because a DFS algorithm is able to "drill" towards a goal, while a BFS takes some time to reach it.  Since optimal path was not in the scope of what I was considering, a DFS was the obvious choice.

### Midpoint

The algorithm uses the most linked to page on Wikipedia (United States) as a midpoint.  This was the central idea of what I believed could make this algorithm efficient.  I would just have to find ANY page that makes its way back to the most popular page.  In theory, this should be far quicker than finding a path between two obscure pages

### Backlinks

The core of the efficiency lies in the backlink approach.  There are two seperate functions: the front-tracking and backtracking functions.  The front-tracking function goes from the start page to the midpoint, while the backtracking function uses backlinks to find a path from the end page to the midpoint.  Once both of them find a path to the midpoint, the paths are combined into a single path.  To make the backtracking even more efficient, I prioritized links that had any mention to the most popular wikipedia page (United States).  Finding one of these links was far quicker than finding a link to the United States itself, and would always result in a path to the United States.

### Testing

To test the program, I would use the https://www.sixdegreesofwikipedia.com/ website to generate sample inputs and to compare my results to theirs.  I exhaustively tested as many links as I could to find errors along the way.  I would also analyze the paths formed by the testing to pinpoint pitfalls and slowdowns of the algorithm. This would also allow me to find further optimizations upon finding certain paths that took longer than others.

## Sample Inputs
Takes an average of 5-10 seconds per input, occasionally up to 30 seconds.  This is a major improvement over the initial code, which was limited to paths of length 2 and could take several minutes to find a path.

Any two links to Wikipedia pages should work, but I'll provide a short list below:

https://en.wikipedia.org/wiki/Dog
https://en.wikipedia.org/wiki/Genus
https://en.wikipedia.org/wiki/Carl_Linnaeus
https://en.wikipedia.org/wiki/Binomial_nomenclature
https://en.wikipedia.org/wiki/Gaspard_Bauhin
https://en.wikipedia.org/wiki/List_of_oldest_universities_in_continuous_operation
https://en.wikipedia.org/wiki/Cyrus_the_Great
https://en.wikipedia.org/wiki/Pasargadae
https://en.wikipedia.org/wiki/Cat



