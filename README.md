# Szymon Kozlowski WikipediaGame

## Installation

Prerequisites: Python, pip

```
git clone https://github.com/szykozlowski/WikipediaGame.git
pip install -r requirements.txt
```

Running/Testing the Program:

```
python Wikipedia_Demo.py
Input name of start page
Input name of end page
I have yet to find 2 pages for which I couldn't find a path; some take a little longer.  Average run time is < 10 seconds. 
```

## How it Works:

Certain pages are much easier to get to than others.  Being able to reach a popular page from both ends of the search results in an efficient path.  The algorithm uses a DFS from both ends. 

From the front, it uses a DFS to drill towards any page with a link to one of the most
popular pages.  This is very quick, as it's nearly guaranteed to find a mention of one of these pages after only a couple of iterations.

From the back, a DFS is used to get backlinks from the end page, and attempts to find a page that is linked to by one of the popular pages.  This takes a bit longer, as the popular pages have a finite amount of pages they link to.  To combat this, the DFS
prioritizes pages that have a mention of the popular page article title.

When the two ends have met in the middle, a path has been created.

## Limitations

- Can be a little slow with certain examples
- Not multi-threaded yet (coming)
- Limited to "United States" as midpoint (although this is part of the reason it's efficient)

## Further Ideas

- Adding multithreading
- Direct Wikipedia API rather than library (this is the primary slowdown)
- Word analysis to pick pages
- List of possible midpoints, which are top 10 articles rather than top 1.  Multithreaded program will record when each side is able to hit one of these, and combine them when they both have reached the same one.

