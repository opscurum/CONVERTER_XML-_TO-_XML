from lxml import etree
import os
import lxml
import requests
from requests.api import request





def create_SubElement(_parent, _tag, attrib=None, _text=None, nsmap=None, **_extra):
    attrib = {} if not attrib else attrib
    result = etree.SubElement(_parent, _tag, attrib, nsmap, **_extra)
    result.text = _text
    return result

def write_xml(tree, xml_name):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)
    tree.write(BASE_DIR + '/' + xml_name, pretty_print=True, xml_declaration=False, encoding="utf-8")


class MyParser:
    def __init__(self, url):
        self.parser = etree.HTMLParser()

        self.page = requests.get(url)

        content = self.page.content
        root = etree.fromstring(content)
        roots = root.xpath('//products')
        goods = etree.Element('Goods')
        for product in roots[0].xpath('//product'):
            
            
           
            good = create_SubElement(goods, 'Good')
            create_SubElement(good, 'GoodId', _text=product.xpath('code')[0].text)
            create_SubElement(good, 'SKU', _text=product.xpath('stock')[0].text)
            create_SubElement(good, 'Ws_code', _text=product.xpath('ws_code')[0].text)
            create_SubElement(good, 'Barkode', _text=product.xpath('barkode')[0].text)
            create_SubElement(good, 'Supplier_code', _text=product.xpath('supplier_code')[0].text)
            create_SubElement(good, 'Cat1name', _text=product.xpath('cat1name')[0].text)
            create_SubElement(good, 'Cat1code', _text=product.xpath('cat1code')[0].text)
            create_SubElement(good, 'Cat2name', _text=product.xpath('cat2name')[0].text)
            create_SubElement(good, 'Cat2code', _text=product.xpath('cat2code')[0].text)
            create_SubElement(good, 'Cat3name', _text=product.xpath('cat3name')[0].text)
            create_SubElement(good, 'Cat3code', _text=product.xpath('cat3code')[0].text)
            create_SubElement(good, 'Cat4name', _text=product.xpath('cat4name')[0].text)
            create_SubElement(good, 'Cat4code', _text=product.xpath('cat4code')[0].text)
            create_SubElement(good, 'Category_path', _text=product.xpath('category_path')[0].text)
            # create_SubElement(good, 'Stock', _text=product.xpath('stock')[0].text)
            create_SubElement(good, 'Unit', _text=product.xpath('unit')[0].text)
            create_SubElement(good, 'Price_list', _text=product.xpath('price_list')[0].text)
            create_SubElement(good, 'Price_list_campaign', _text=product.xpath('price_list_campaign')[0].text)
            create_SubElement(good, 'Price_special_vat_included', _text=product.xpath('price_special_vat_included')[0].text) 
            create_SubElement(good, 'Special_price', _text=product.xpath('special_price')[0].text) 
            create_SubElement(good, 'Price_special_rate', _text=product.xpath('price_special_rate')[0].text) 
            create_SubElement(good, 'Min_order_quantitiy', _text=product.xpath('min_order_quantitiy')[0].text) 
            create_SubElement(good, 'Price_credit_card', _text=product.xpath('price_credit_card')[0].text) 
            create_SubElement(good,  'Vat', _text=product.xpath( 'vat')[0].text) 
            create_SubElement(good,  'Desi', _text=product.xpath( 'desi')[0].text)
            create_SubElement(good, 'Width', _text=product.xpath('width')[0].text)
            create_SubElement(good,  'Delivery_date', _text=product.xpath( 'delivery_date')[0].text)
            create_SubElement(good, 'Detail', _text=product.xpath('detail')[0].text)
            create_SubElement(good, 'Seo_title', _text=product.xpath('seo_title')[0].text)
            create_SubElement(good, 'Seo_description', _text=product.xpath('seo_description')[0].text)
            create_SubElement(good, 'Seo_keywords', _text=product.xpath('seo_keywords')[0].text)
            
            
             
            
            
           
            
            
            images = create_SubElement(good, 'Images')
            
            
            create_SubElement(images, 'Src', _text=product.xpath('image')[0].text)
            additional_images = product.xpath("*[starts-with(local-name(), 'additional_image_')]")
            for additional_image in additional_images:
                print(additional_image.text)
                create_SubElement(images, 'Src', _text=additional_image.text)
                
            variants = create_SubElement(good, 'Variants')
            
            for option in product.xpath('options')[0].xpath('option'):
                variant = create_SubElement(variants, 'Variant')

                create_SubElement(variant, 'options1', _text=option.xpath('VaryantGroupId')[0].text)
                create_SubElement(variant, 'options2', _text=option.xpath('code')[0].text) 
                create_SubElement(variant, 'options3', _text=option.xpath('type1')[0].text)
                create_SubElement(variant, 'options4', _text=option.xpath('type2')[0].text)
                create_SubElement(variant, 'options5', _text=option.xpath('barcode')[0].text)
                create_SubElement(variant, 'options6', _text=option.xpath('stock')[0].text)
                create_SubElement(variant, 'options7', _text=option.xpath('desi')[0].text)
                create_SubElement(variant, 'options8', _text=option.xpath('price_list')[0].text)
                create_SubElement(variant, 'options9', _text=option.xpath('price_list_discount')[0].text)
                create_SubElement(variant, 'options10', _text=option.xpath('price_special')[0].text)
                create_SubElement(variant, 'options11', _text=option.xpath('supplier_code')[0].text)
                
                

        new_tree = etree.ElementTree(goods)
        write_xml(new_tree, 'guncel_klas.xml')

if __name__ == '__main__':
    MyParser(url='https://klasayakkabi.com/index.php?route=feed/universal_feed&feed=klas.xml')
