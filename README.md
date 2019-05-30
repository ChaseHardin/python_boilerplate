# Local Development

## Configure Pyenv
* Follow [docs](https://github.com/pyenv/pyenv) to install Pyenv.
* Ensure the following commands were run:
```
brew install pyenv
brew install pyenv-virtualenv
```

* Install Python on Pyenv by running: `pyenv install 3.7.3`
* Create virtual environment by running: `pyenv virtualenv 3.7.2 <virtual_environment_name>`
* Add `eval "$(pyenv init -)"` to `.zshrc`.
* Activate virtualenv by running: `pyenv activate <virtual_environment_name>`
* Configure interpretor to the virtual environment

## Install Spark/PySpark
* Add apache-spark, `brew install apache-spark`
* add java 8, `brew cask install caskroom/versions/java8`
* Verify install by running `pyspark` in the terminal.
* Helpful resource used to install PySpark can be found [here](https://medium.com/@yajieli/installing-spark-pyspark-on-mac-and-fix-of-some-common-errors-355a9050f735)

#### Resolved Errors
* Error: `jupyter: No such file or directory`
    * To resolve when using Python 3: `pip3 install --upgrade --force-reinstall --no-cache-dir jupyter`
    
    
## PyCharm Configuration
* https://stackoverflow.com/questions/34685905/how-to-link-pycharm-with-pyspark

## Install Requirements
* Run `pip install -r requirements.txt`