# shorty_erl

Shorten URLs or fetch full URLs.

requires the [requests](http://docs.python-requests.org/) library. should work on python 3.6+.

### install

`pip3 install .`

### usage

General usage:

```
usage: shorty_erl.py [-h] [-u URL] [-s SHORTEN] [-us UNSHORTEN]

Shorten URLs or fetch full URLs.

required arguments:
  -u , --url        URL

possible actions (at least one is required):
  -s, --shorten     Shorten URL
  -us, --unshorten  Check URL shorten status

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show program's version number and exit
```

shorten URL:
`python3 shorty_erl.py -u <full_url> -s`

Get last 3 GitHub pull requests:
`python3 shorty_erl.py -u <short_url> -us`

##### Troubleshooting

Upgrade pip with `pip3 install -U pip` if the following error occurs:

`Directory '.' is not installable. File 'setup.py' not found.`
