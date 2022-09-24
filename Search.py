import argparse
import sys


def unique_index(list_index: list) -> list:
    list_set = set(list_index)
    return list(list_set)


def list_to_string(list_index: list) -> str:
    str1 = ","
    if len(list_index) != 0:
        list_index.sort()
        list_string = map(str, list_index)
        return str1.join(list_string)
    else:
        return "No result found"


def search_by_type_or(query_content: list) -> list:
    references = []
    for list_index in data_into_list:
        for query_content_index in query_content:
            if list_index.find(query_content_index) != -1:
                current_search_index = data_into_list.index(list_index)
                references.append(current_search_index)

    unique_list_index = unique_index(references)
    return unique_list_index


def search_by_type_and(query_content: list) -> list:
    references = []
    for list_index in data_into_list:
        for query_content_index in query_content:
            if list_index.find(query_content_index) != -1:
                current_search_index = data_into_list.index(list_index)
                references.append(current_search_index)

    duplicate_item = [x for i, x in enumerate(references) if i != references.index(x)]
    unique_list_index = unique_index(duplicate_item)
    return unique_list_index


def search(query: str, query_type: str) -> str:

    query_content = query.split()

    type_or = ["or", "Or", "OR", "oR"]
    type_and = ["and", "AND"]

    references = []
    if query_type in type_or:
        references = search_by_type_or(query_content)
    if query_type in type_and:
        references = search_by_type_and(query_content)

    result = list_to_string(references)
    print(result)


def main(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--query', help='Specify search query. Needs to be a string', required=True)
    parser.add_argument('-t', '--type', help='Specify type of search: "and" or "or"', required=True)

    args = parser.parse_args(args)

    if args.query is None:
        parser.error('Please specify your search query (-q).')

    if args.type is None:
        parser.error('Please specify your type of search query (-t).')
    search(args.query, args.type)


if __name__ == "__main__":
    try:
        with open("hscic-news", "r") as file:
            # read all content from a file using read()
            content = file.read()
            # split file content into list of strings
            data_into_list = content.split("\n")
            file.close()

    except FileNotFoundError:
        print("The file was not found")
    sys.exit(main(sys.argv[1:]))
    # sys.exit(main())


