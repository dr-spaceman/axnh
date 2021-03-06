# AXRN Animal Crossing New Horizons Right Now

An app for [Animal Crossing: New Horizons](https://www.nintendo.com/games/detail/animal-crossing-new-horizons-switch/) players to show what critters are available rn, and to list all available critters based on month, time of day, and location. Also events (holidays, birthdays, NPC visits, etc.) if time permits.

## Built With

* Python 3
* [Flask v1.1](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Beautiful Soup v4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scraping
* [Jinja 2](https://jinja.palletsprojects.com/en/2.11.x/) - Templating
* [SCSS](https://sass-lang.com/) - CSS preprocessing

## Launch

Dependencies listed in [requirements.txt](requirements.txt); Set up your virtual environment: `pip install -r requirements.txt`

## Contributing

Contributions welcome!

### Code of Conduct

All fruits are created equal, especially pears. No fruit discrimination allowed. This is a safe place. [#peargang](https://twitter.com/hashtag/peargang)4life

## Authors

* **Matt Berti** - *Initial work* - [Dr Spaceman](https://github.com/dr-spaceman)
* Your name here

## Acknowledgments

* Data provided by [Animal Crossing Wiki | Fandom](https://animalcrossing.fandom.com/wiki/Animal_Crossing_Wiki) 
* Runner.py compiler & minimizer inspired by [Julian Nash](https://pythonise.com/categories/python/python-minify-js-css-compile-scss)

## Todo

* Back end
    * [x] Compile critter data
        * [x] Scrape Animal Crossing Wiki
    * [x] Flask app
    * [ ] Determine/switch Hemisphere (rn it's only North, sorry Southern friends :/)
    * [ ] Events
* Front end
    * [x] Responsive CSS, mobile-first
        * [x] Issue: All critters data tables extend page width
            * Media query that converts <table> to box elements
    * [x] CSS Grid