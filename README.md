# shorty

A minimal Python script to shorten DOIs in bibtex files using http://shortdoi.org/. The shortener is offered by the [International DOI Foundation](https://www.doi.org/). 

## What does it do?

It converts

```bib
@article{Moritz2018,
    doi = {10.1109/tvcg.2018.2865240},
    year  = {2018},
    publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
    author = {Dominik Moritz and Chenglong Wang and Greg L. Nelson and Halden Lin and Adam M. Smith and Bill Howe and Jeffrey Heer},
    title = {Formalizing Visualization Design Knowledge as Constraints: Actionable and Extensible Models in Draco},
    journal = {{IEEE} Transactions on Visualization and Computer Graphics}
}
```

to (notice the shorter DOI!)

```bib
@article{Moritz2018,
	doi = {10/cs68},
	year  = {2018},
	publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
	author = {Dominik Moritz and Chenglong Wang and Greg L. Nelson and Halden Lin and Adam M. Smith and Bill Howe and Jeffrey Heer},
	title = {Formalizing Visualization Design Knowledge as Constraints: Actionable and Extensible Models in Draco},
	journal = {{IEEE} Transactions on Visualization and Computer Graphics}
}
```

## Why do I want to use it?

You may have a page limit or you just want your references to be shorter to fit on a single (or two, or three, or n) page. 

## How do I use it?

Download [the script](main.py). Then copy your bibtex file to a new file (here `demo.bib` but you can call it `long.bib`). Then run

```
python main.py demo.bib > short.bib
```

Alternatively, you can pipe in the the content

```
cat demo.bib python main.py > short.bib
```
