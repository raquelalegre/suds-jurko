# Python's SUDS example

Teaching myself some SOAP with __[SUDS](https://fedorahosted.org/suds/wiki/Documentation)__.

This will be needed by one of the projects I work on at UCL called [ORACC](https://github.com/UCL-RITS/nammu).

To run this example you need to install _SUDS_, for example: `pip install suds`.

To run the examples:

```
git clone https://github.com/raquel-ucl/suds-example.git
cd suds-example
python client.py <url_to_wsdl>
```

This will print out the list of method signatures accesible from the given url and their parameters.

__Important note__: `suds` seems to not be maintained anymore. Luckily, someone has been contributing trying to keep it updated in a parallel repo until `suds`' developers revive development. The development package for `suds` is known as __[suds-jurko](https://bitbucket.org/jurko/suds)__. To install it you have to make sure `suds` is not installed (e.g. `pip uninstall suds`) and install `suds-jurko` (e.g. `pip install suds-jurko`). To use it, you just need to do `import suds` and it'll automatically link to `suds-jurko`. 




