Drawpile.net website
---------------------

This is the source code to the drawpile.net website.

## Setup

First, create a database for the site. (The official site uses
PostgreSQL, but MySQL or even SQLite should also work for development)

Next, create a Python 3 virtualenv for the project and run `pip install -r requirements.py`

Copy `drawpile/local_settings.sample` to `drawpile/local_settings.py` and
edit to suit your environment.

Run `./manage.py migrate` to initialize the database.  
Run `./update-assets.sh` to populate the database with the basic content.

You should now have a local copy of the website, ready for development!

### Deployment

TODO

## Django apps

This project is made up of the following custom Django apps.

### Templatepages

This app contains utilities for creating (mostly) static pages using Django templates.

The following things are stored in database:

 * Images: uploadable images for which thumbnails can be generated.
 * Template variables: Fetch key/value pairs from the database

Management commands are provided to help manage uploaded images and templatevars.

### News

This is a very simple blog engine used for the news page.

A management command for importing and exporting posts is included.

## License

The source code is licensed under the MIT license.
The static website page content (article text and illustrations) is licensed Creative Commons Attribution-ShareAlike 4.0

