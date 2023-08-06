# crossref-citedby-driver

Library containing driver logic for the HIRMEOS crossref-citedby-driver.


Until CI is ready

.. code-block:: bash

    $ python3 setup.py sdist bdist_wheel
    $ twine upload dist/*


Release Notes:

[0.0.5] - 2023-07-26

Added:
    * Better "best guess" for crossref DOI published date
    * Determine the prime-doi for an aliasd DOI

Changed:
    * Switched project to using build and toml configuration

[0.0.4] - 2023-06-09

Added:
    * Unittests

Changed:
    * Set `feature` to "xml" rather than "lxml" when reading XML using BeautifulSoup

[0.0.3] - 2022-03-24

Changed:
    * Update requirements

[0.0.2] - 2022-03-24

Changed:
    * Update requirements
