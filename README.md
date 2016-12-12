# common-dibbs

## Generate clients

Clients are generated from swagger yaml description files (http://swagger.io/). To generate a swagger client, you will need to install the swagger-codegen project. On MacOS, simply run the following command:

```shell
brew install swagger-codegen
```

Then, to generate the python clients, run the following command:

```shell
bash rebuild_clients.sh
```


## Install clients

Run the following command:

```shell
pip install .
```

## Publish clients

Run the following command:

```shell
python setup.py install sdist upload -r pypi
```
*Don't forget to increase the version number of the **setup.py** file*

