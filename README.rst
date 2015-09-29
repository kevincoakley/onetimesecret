#############
onetimesecret
#############

.. image:: https://travis-ci.org/kevincoakley/onetimesecret.svg?branch=master
    :target: https://travis-ci.org/kevincoakley/onetimesecret


************
Installation
************

Install via pip:

::

    $ pip install git+https://github.com/kevincoakley/onetimesecret.git

Install from source:

::

    $ git clone https://github.com/kevincoakley/onetimesecret.git
    $ cd onetimesecret
    $ python setup.py install

*******
Removal
*******

Remove via pip:

::

    $ pip uninstall onetimesecret -y

********
Commands
********

**onetimesecret-userpass**

Example Usage:

::

    $ onetimesecret-userpass -u user -o pass
    
And will create the following onetimesecret secret:

::

    username: user
    password: pass
    
**onetimesecret-openstack**

Example Usage:

::

    $ onetimesecret-openstack -a http://url:5000/v2 -t project -u user -o pass
  
 
And will create the following onetimesecret secret:

::
    
    os-auth-url: http://url:5000/v2
    os-tenant-name: project
    os-username: user
    os-password: pass

And will create the following onetimesecret secret:

::

    username: user
    password: pass
    
**onetimesecret-csv**

Example Usage:

::

    $ onetimesecret-csv -i input.csv -o output.csv

Example input CSV:

::

    username,password
    user1,pass1
    user2,pass2
    
Will output CSV:

::

    username,password
    user1,pass1,http://onetimesecret.com/secret/12345
    user2,pass2,http://onetimesecret.com/secret/67890

And will create onetimesecret secrets where the header columns are the item titles and the rows are the item variables:

::

    username: user1
    password: pass1
    
::

    username: user2
    password: pass2

