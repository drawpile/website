Drawpile.net website
---------------------

This is the source code to the drawpile.net website.

## Setup

First, create a database for the site. (The official site uses
PostgreSQL, but MySQL or even SQLite should also work for development)

Next, create a Python 3 virtualenv for the project and run `pip install -r requirements.txt`

Copy `drawpile/local_settings.sample` to `drawpile/local_settings.py` and
edit to suit your environment.

Run `./manage.py migrate` to initialize the database.  
Run `./update-assets.sh` to populate the database with the basic content.

Run './manage.py dpauth' to generate a keypair for external authentication. Copy&paste
the output into your `local_settings.py` file.

You should now have a local copy of the website, ready for development!

### Deployment

Install gunicorn in the virtualenv:

    `pip install gunicorn`

See the file `website.service` for a sample systemd unit file for running gunicorn.

Configure nginx to proxy the site:

	server {
		... server configuration ...

		location / {
			proxy_pass http://127.0.0.1:8000/;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header Host $http_host;
			proxy_redirect off;
		}

		# Static files
		location /media {
			alias /home/website/website/allstatic;
		}

		# Release archive
		location /files {
			alias /home/webfiles/www;
			access_log /var/log/nginx/files_access.log;
			autoindex on;
		}
	}

See also: http://docs.gunicorn.org/en/stable/deploy.html

Finally, remember to run `./manage.py collectstatic` to gather all static files in one place.

## Django apps

This project is made up of the following custom Django apps.

### Dpauth

This app contains the external authentication/single sign on implementation.
Other than the external deps listed below, it is completely self contained
and is custom user model aware, so it can be easily used in other projects
with no modification.

The management command `dpauth` will generate a random public
and private keypair for signing login tokens. See also `dpauth/settings.py`
for adjustable settings.

This app has the following external dependencies:

 * Django Rest Framework
 * Ed25519
 * Confusable_homoglyphs

### Dpusers

User account related stuff. Login, signup and profile editing views.

### Templatepages

This app contains utilities for creating (mostly) static pages using Django templates.

The following things are stored in database:

 * Images: uploadable images for which thumbnails can be generated.
 * Template variables: Fetch key/value pairs from the database

Management commands are provided to help manage uploaded images and templatevars.

### News

This is a very simple blog engine used for the news page.

A management command for importing and exporting posts is included.

## Django permissions

The following Django permissions are used outside the admin site:

 * `dpauth.moderator` - global Drawpile moderator

## License

The source code is licensed under the MIT license.
The static website page content (article text and illustrations) is licensed Creative Commons Attribution-ShareAlike 4.0

