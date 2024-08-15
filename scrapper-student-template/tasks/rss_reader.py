# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json as j

class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        #>>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        #>>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        #>>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """

    limit = limit
    root = ET.fromstring(xml).find('channel')
    output = {
        'title': None if root.find('title') is None else root.find('title').text,
        'link': None if root.find('link') is None else root.find('link').text,
        'lastBuildDate': None if root.find('lastBuildDate') is None else root.find('lastBuildDate').text,
        'pubDate': None if root.find('pubDate') is None else root.find('pubDate').text,
        'language': None if root.find('language') is None else root.find('language').text,
        'categories': None if root.findall('category') == [] else [c_category.text for c_category in
                                                                   root.findall('category')],
        'editor': None if root.find('managinEditor') is None else root.find('managinEditor').text,
        'description': None if root.find('description') is None else root.find('description').text,
        'items': None if root.findall('item') == [] else [{'title': None if item.find('title') is None
        else item.find('title').text,
                                                           'author': None if item.find('author') is None
                                                           else item.find('author').text,
                                                           'pubDate': None if item.find('pubDate') is None
                                                           else item.find('pubDate').text,
                                                           'link': None if item.find('link') is None
                                                           else item.find('link').text,
                                                           'categories': None if item.findall('category') == []
                                                           else [category.text
                                                                 for category in item.findall('category')],
                                                           'description': None if item.find('description') is None
                                                           else item.find('description').text,
                                                           } for num, item in enumerate(root.findall('item'))][:limit]
    }

    if json:
        return [j.dumps(output, indent=2)]
    else:
        result = [
            f"Feed: {output['title']}",
            f"Link: {output['link']}",
            f"Description: {output['description']}"
        ]
        if output['items'] is not None:
            for i in output['items']:
                result.append(f"\nTitle: {i['title']}")
                result.append(f"Published: {i['pubDate']}")
                result.append(f"Link: {i['link']}")
                if i['description'] is not None:
                    result.append(f"description: {i['description']}")

        return result


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text

    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
