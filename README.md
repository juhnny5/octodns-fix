# octodns-fix

When you import a zone (using the `--lenient` option), it may contain errors that are sometimes difficult to resolve.

Very often the problem is that the "." at the end of the CNAME is missing. When you have a very large number of records, this script is here to help you fix this error.

## Usage

How to use it :

```
chmod u+x octodns-fix.py
./octodns-fix.py --file example.org.yaml
```

Your file will be automatically corrected. All that's left is to apply your changes.
