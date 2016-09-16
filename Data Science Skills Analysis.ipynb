{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from urllib2 import urlopen\n",
    "import feedparser\n",
    "from collections import Counter\n",
    "from nltk.tokenize import RegexpTokenizer\n",
    "import re\n",
    "import pdb\n",
    "\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "FEED_URL='http://www.indeed.com/jobs?q=data+scientist&l=New+York%2C+NY' \n",
    "fp = feedparser.parse(FEED_URL)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fp = feedparser.parse(FEED_URL)\n",
    "soup = BeautifulSoup(fp['feed']['summary'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#method accepts a BeautifulSoup parsed HTML object and returns a list of <a> tags of job posts\n",
    "def get_job_posts(soup_object):\n",
    "    \n",
    "    job_posts = []\n",
    "    a_s = soup_object.find_all('a')\n",
    "    for a in a_s:\n",
    "        try:\n",
    "            if u'jobtitle' in a['class']:\n",
    "                job_posts.append(a)\n",
    "        except:\n",
    "            pass\n",
    "    \n",
    "    return job_posts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#method accepts a link to a job post and returns a list of \n",
    "def get_words(job_post_href):\n",
    "    \n",
    "    #only keep the content\n",
    "    post_soup = BeautifulSoup(feedparser.parse(job_post_href)['feed']['summary'], 'html.parser')\n",
    "\n",
    "    text = post_soup.get_text().lower()\n",
    "    \n",
    "    #keep only letters, but keep '+' for 'c++', '#' for 'c#','3' for 'd3, '!' for 'go!', and  '-' for 'scikit-learn'\n",
    "    text = re.sub(\"[^a-z+#3-]\",\" \", text) \n",
    "\n",
    "    #break into lines to get rid of the annoying '\\n' characters. Also project to lowercase.\n",
    "    lines = [line.strip().lower() for line in text.splitlines()]\n",
    "\n",
    "    words = []\n",
    "    for line in lines:\n",
    "        words += [each_word for each_word in line.split()]\n",
    "        \n",
    "    #Lighten the load by getting rid of basic stopwords, like \"the\", \"or\" etc    \n",
    "    words = set(words) - set(nltk.corpus.stopwords.words(\"english\")) \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#method accepts a list of words in a job post, and creates sets according to pre-determined sets\n",
    "def words_by_category(words_list):\n",
    "    \n",
    "    high_level_languages = set(['r', 'python', 'java', 'scala', 'c', 'c++', 'c#', 'c--', \n",
    "                               'f', 'f#', 'go', 'go!', 'groovy', 'julia', 'jscript', \n",
    "                               'matlab', 'perl'])\n",
    "    \n",
    "    low_level_langages = set(['pascal', 'haskell', 'fortran', 'django', 'flask'])\n",
    "    \n",
    "    frameworks = set(['angular', 'angularjs', 'asp', 'node' ])\n",
    "    \n",
    "    #operating systems and tools\n",
    "    operating_systems = set(['unix', 'osx', 'bash', 'batch' , 'curl' ])\n",
    "    \n",
    "    misc_tools = set(['latex' ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def crawl_indeed(query, city, experience_level = \"\", num_pages = 10):\n",
    "    \n",
    "    #clean parameters so that they match Indeed's protocol\n",
    "    \n",
    "    #spaces parameters seperated by '+'\n",
    "    query = query.replace(' ', '+')\n",
    "    city = city.replace(' ' , '+')\n",
    "    \n",
    "    #make sure experience_level is one of the four valid options\n",
    "    if experience_level not in ['', 'entry_level', 'mid_level', 'senior_level']:\n",
    "        experience_level = ''\n",
    "        print \"Experience level parameter not valid. Showing all experience levels\"\n",
    "    \n",
    "    #build data in JSON-like format, given the heirarchial nature of the data\n",
    "    data = list()\n",
    "    \n",
    "    #Indeed shows job posts 10 at a time, so each page starts with post 0, 10, 20...\n",
    "    #Loop through the posts using the num_pages parameter\n",
    "    \n",
    "    page_start_numbers = np.arange(num_pages)*10\n",
    "    \n",
    "    for start_number in page_start_numbers:\n",
    "        \n",
    "        url = \"http://www.indeed.com/jobs?q={0}&l={1}&explvl={2}&start={3}\".format(query, city, experience_level, start_number)\n",
    "    \n",
    "        #isolate html body and get rid of extraneous HTML objects using feedparser, and create a BeautifulSoup obect\n",
    "        fp = feedparser.parse(url)\n",
    "        page_soup = BeautifulSoup(fp['feed']['summary'])\n",
    "    \n",
    "        #get a list of all the <a class='jobtitle'></a> elemdents, which are job posts\n",
    "        job_posts = get_job_posts(page_soup)\n",
    "\n",
    "        for post in job_posts:\n",
    "            \n",
    "            #each job post gets a sub-dictionary\n",
    "            post_data = dict()\n",
    "            \n",
    "            #attributes which are constant amongst all results\n",
    "            post_data['query'] = query\n",
    "            post_data['city'] = city\n",
    "            \n",
    "            #job title of that sepcific post\n",
    "            post_data['title'] = post['title']\n",
    "            \n",
    "            \n",
    "            #for each job post, extract the link to the post itself\n",
    "            post_href = post['href']\n",
    "            \n",
    "            #extract all the (cleaned up) words fromt that link\n",
    "            post_words = get_words(post_href)\n",
    "            \n",
    "            pdb.set_trace()\n",
    "            \n",
    "            post_data['words'] =post_words\n",
    "            data.append(post_data)\n",
    "            \n",
    "            \n",
    "        pdb.set_trace()\n",
    "    #http://www.indeed.com/jobs?q=data+scientist&l=New+York,+NY&explvl=entry_level\n",
    "    #http://www.indeed.com/jobs?q=data+scientist&l=New+York,+NY&explvl=senior_level&start=0\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "> <ipython-input-129-4d003a18fd7c>(6)get_words()\n",
      "-> post_soup = BeautifulSoup(feedparser.parse(job_post_href)['feed']['summary'], 'html.parser')\n",
      "(Pdb) c\n",
      "> <ipython-input-134-2d287d37d927>(54)crawl_indeed()\n",
      "-> post_data['words'] =post_words\n",
      "(Pdb) c\n",
      "> <ipython-input-129-4d003a18fd7c>(6)get_words()\n",
      "-> post_soup = BeautifulSoup(feedparser.parse(job_post_href)['feed']['summary'], 'html.parser')\n",
      "(Pdb) c\n",
      "> <ipython-input-134-2d287d37d927>(52)crawl_indeed()\n",
      "-> pdb.set_trace()\n",
      "(Pdb) data\n",
      "[{'query': 'data+scientist', 'title': u'Machine Learning Quantitative Analyst', 'words': None, 'city': 'new+york'}]\n",
      "(Pdb) q\n"
     ]
    },
    {
     "ename": "BdbQuit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mBdbQuit\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-135-e9f3be768181>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mcrawl_indeed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'data scientist'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'new york'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-134-2d287d37d927>\u001b[0m in \u001b[0;36mcrawl_indeed\u001b[0;34m(query, city, experience_level, num_pages)\u001b[0m\n\u001b[1;32m     50\u001b[0m             \u001b[0mpost_words\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_words\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpost_href\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 52\u001b[0;31m             \u001b[0mpdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_trace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m             \u001b[0mpost_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'words'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0mpost_words\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-134-2d287d37d927>\u001b[0m in \u001b[0;36mcrawl_indeed\u001b[0;34m(query, city, experience_level, num_pages)\u001b[0m\n\u001b[1;32m     50\u001b[0m             \u001b[0mpost_words\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_words\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpost_href\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 52\u001b[0;31m             \u001b[0mpdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_trace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m             \u001b[0mpost_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'words'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0mpost_words\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bdb.pyc\u001b[0m in \u001b[0;36mtrace_dispatch\u001b[0;34m(self, frame, event, arg)\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;31m# None\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mevent\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'line'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 49\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdispatch_line\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mevent\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'call'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdispatch_call\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bdb.pyc\u001b[0m in \u001b[0;36mdispatch_line\u001b[0;34m(self, frame)\u001b[0m\n\u001b[1;32m     66\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstop_here\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbreak_here\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     67\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser_line\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 68\u001b[0;31m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquitting\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;32mraise\u001b[0m \u001b[0mBdbQuit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     69\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtrace_dispatch\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     70\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mBdbQuit\u001b[0m: "
     ]
    }
   ],
   "source": [
    "crawl_indeed('data scientist', 'new york')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "a = set([1,4,2,6])\n",
    "b = set([3,5,4,2,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 3, 4, 5, 6}"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a and b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "job_post_href = 'https://careers.bloomberg.com/job/detail/54015?utm_source=Indeed&utm_campaign=Bloomberg_Indeed&sponsored=ppc&utm_campaign=SalesUS'\n",
    "feedparser.parse(job_post_href)\n",
    "\n",
    "post_soup = BeautifulSoup(feedparser.parse(job_post_href)['feed']['summary'], 'html.parser')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
