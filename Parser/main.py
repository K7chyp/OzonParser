from BaseClassPage import OzonPageParser


def main():
    print(
        OzonPageParser(
            'https://www.ozon.ru/product/gazonokosilka-gardena-powermax-1400-34-elektricheskaya-140052491/'
        ).hrefs_to_products_at_page
    )


if __name__ == "__main__":
    main()
    
