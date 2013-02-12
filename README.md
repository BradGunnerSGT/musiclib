# MusicLib

MusicLib is a music library organization tool to allow performance
organizations the ability to catalog their music libraries and annotate every
performance of each music title.

## Requirements

MusicLib is built off of the [Django web framwork](http://djangoproject.com) version 1.4 and requires Django to be available prior to installation.

If you have questions on how to install Django or any of its components, please see the excellent [installation documentation](https://docs.djangoproject.com/en/1.4/topics/install/)

### Requirements

- Django 1.4 (tested on 1.4.3)
- South (a Django extension used for data migrations)
- Python &gt;= 2.6 (Django requires 2.5, however we use a few features introduced in 2.6)
- A database supported by Django (MySQL, Sqlite3, Postgresql)
- A wsgi-compatible web server such as Apache

## Installation


### Installing on Windows

1. Install Django and its requirements.  MusicLib supports using the
   [Django Stack](http://bitnami.org/stack/django) by Bitnami, which
   includes Python, Django, Apache, and MySQL in a single installable Windows
   package.
2. Install Django South (TODO instructions here)
3. Unzip the MusicLib install zipfile into <code>C:\musiclib\app



### Installing Django on Unix/Linux

#### Install Django on RHEL/Centos

RHEL/CentOS users will need to add the [EPEL repository](http://fedoraproject.org/wiki/EPEL) prior to running these commands.

Note: Make sure you type this exactly as presented, notice the uppercase "D" in this command.

<code>
sudo yum install Django Django-south mysql
django-admin.py --version
</code>

#### Install Django on Fedora

<code>
sudo yum install python-django python-django-south mysql
django-admin --version
</code>

#### Install Django on Debian/Ubuntu

<code>
sudo apt-get install python-django python-django-south mysql
django-admin --version
</code>

### Install MusicLib

1. Install Django and its requirements as per the previous section of documentation.
2. Unzip the musiclib-$version.zip zipfile into <code>


## First-time configuration of Musiclib


django-admin

TODO: add more info here
