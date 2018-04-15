# Stats4R

Stats4R shows you the vital statistics of [Reddit's most popular online dating sub.](https://www.reddit.com/r/r4r)

It is a web scraper and data analysis program written specefically for [/r/r4r](https://www.reddit.com/r/r4r).

# Features

### Demographics
__Gender Distribution__
![Gender distribution plot]("https://github.com/sharmaeshaan/Stats4R/blob/dev/screenshots/population.png")
__Average Age__
![Average age plot]("https://raw.githubusercontent.com/sharmaeshaan/Stats4R/dev/screenshots/ages.png")
### Who's Seeking Who
![Who's seeking who plot]("https://github.com/sharmaeshaan/Stats4R/blob/dev/screenshots/seeking.png")
### Interaction
__Comments on Posts: Males VS Females__
![Average comments plot]("https://github.com/sharmaeshaan/Stats4R/blob/dev/screenshots/comments.png")
__Upvotes to Posts: Males VS Females__
![Average upvotes plot]("https://github.com/sharmaeshaan/Stats4R/blob/dev/screenshots/upvotes.png")

---

# Getting Started

## Requirements

Stats4R is built with **Python 3**.  You can check your version of Python by entering the following command in a terminal window:
```
python --version
```
If your system does not have Python or has Python 2, please [download and install]((https://www.python.org/downloads/)) the latest version of Python 3.

**The following Python libraries are required to run Stats4R:**
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
```
pip install beautifulsoup4
```
- [Requests](http://docs.python-requests.org/en/master/user/install/#install)
```
pip install requests
```
- [Matplotlib](https://matplotlib.org/users/installing.html)
```
pip install matplotlib
```
- [Flask](http://flask.pocoo.org/)
```
pip install Flask
```
*If you have the [Anaconda distribution of Python](https://www.anaconda.com/download/) you won't need to install the above requirements.*

--- 

## Running Stats4R

Running Stats4R is simple.
### __MacOS and Linux__
1. Download the repository and unzip it to your desired location
2. Navigate to the unzipped folder and open a terminal window
3. Enter the command below:
```
./stats4r.sh
```
4. Sit back and wait. Depending on your internet connection Stats4R should take approximately 20 minutes to crawl 25 pages of [/r/r4r](https://www.reddit.com/r/r4r) and analyze about 600 posts

4. Open your browser and go to http://localhost:5000/ or http://127.0.0.1:5000/

To quit, press `ctrl + c` in the terminal window where the program is running.

### __Windows__

Windows users can run Stats4R by running the Python scripts __in the following sequence__, with the commands below:
```
python spider_r4r.py
```
```
python analyse_r4r.py
```
```
python plot_r4r.py
```
```
python front_r4r.py
```
_A `.bat` file will be created soon to run the program with a single command._

---

# Contributing

Please feel free to make pull requests or fork the repo. 

For any feature requests or suggestions, send a message at sharmaeshaanw@gmail.com -- critical feedback is welcome!

Star the repo if you liked the project :star:

If you're interested in doing something similar to Stats4R, I'd love to talk about it!  :raised_hands: