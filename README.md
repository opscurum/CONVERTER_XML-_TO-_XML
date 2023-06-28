# XML Parser

This Python script provides functionality for parsing XML data from a specified URL and generating a new XML file. The script utilizes the `lxml` library to handle XML parsing and manipulation.

## Prerequisites

Make sure you have the following dependencies installed:

- `lxml`
- `requests`

You can install them by running the following command:

```shell
pip install lxml requests
```

## Usage

To use the XML parser, follow these steps:

1. Import the necessary libraries:
   ```python
   from lxml import etree
   import os
   import requests
   ```

2. Define the `create_SubElement` function:
   - This function creates a new subelement under a parent element and sets its attributes and text.
   - The function takes parameters such as `_parent` (parent element), `_tag` (tag name), `attrib` (element attributes), `_text` (element text), and `nsmap` (namespace mapping).
   - The function returns the newly created subelement.

3. Define the `write_xml` function:
   - This function writes the XML tree to a file.
   - The function takes parameters such as `tree` (XML tree object) and `xml_name` (name of the XML file to be generated).
   - The function writes the XML tree to the specified file path, with optional pretty printing, XML declaration, and encoding settings.

4. Define the `MyParser` class:
   - This class represents the XML parser.
   - The class constructor takes a URL parameter, which specifies the URL of the XML data to be parsed.
   - Inside the constructor, the XML data is fetched from the URL using the `requests` library.
   - The XML content is then parsed using the `lxml` library, and the root element is obtained.
   - The necessary elements and attributes are extracted from the XML data and used to create a new XML tree structure.
   - The newly created XML tree is then written to a file using the `write_xml` function.

5. Instantiate the `MyParser` class with the desired URL:
   ```python
   if __name__ == '__main__':
       MyParser(url='https://klasayakkabi.com/index.php?route=feed/universal_feed&feed=klas.xml')
   ```

Ensure that you replace the URL in the `MyParser` instantiation with the desired XML data source.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

The XML parsing functionality in this script is made possible by the `lxml` and `requests` libraries. Thanks to the developers of these libraries for their contributions.
