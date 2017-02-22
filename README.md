<p align="center">
  <img src="http://imgur.com/M5Ix4sQ.png" alt="unfetch">
  <br>
  <a href="https://travis-ci.com/tijme/not-your-average-web-crawler">
    <img src="https://travis-ci.com/tijme/not-your-average-web-crawler.svg?token=CRkUqxZ8WNMhxZYQUj18&amp;branch=master" alt="Build Status">
  </a>

  <a href="/tijme/not-your-average-web-crawler/blob/master/LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>

</p>

## Description
N.Y.A.W.C is a Python 3 application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request and keeps track of the request data. It's main purpose is to be used in web application vulnerability scanners like [Angular CSTI scanner](https://github.com/tijme/angular-csti-scanner).

## Usage
First make sure you're on Python 3.5 or higher. Then run the command below to install the dependencies.

`pip install -r requirements.txt`

ToDo: explain how this module can be implemented and used in another project.

## Testing

The testing can and will automatically be done by [Travis CI](https://travis-ci.com/) on every push to the master branch. If you want to manually run the unit tests, usage the command below.

`python -m unittest discover -s tests`.

## License

Not Your Average Web Crawler (N.Y.A.W.C) is open-sourced software licensed under the [MIT license](LICENSE.md).
