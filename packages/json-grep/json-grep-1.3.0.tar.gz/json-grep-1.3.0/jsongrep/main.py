import os
import signal
import sys
from argparse import ArgumentParser
from jsongrep.libs.setuptools import get_file_content
from jsongrep.libs.json_filter import JsonFilter, JsonFilterException


def _handle_exit(sig, frame):
    print('Terminated.')
    sys.exit(0)


def _handle_args() -> tuple:
    version = get_file_content(os.path.join(os.path.dirname(__file__), "VERSION"))
    parser = ArgumentParser(description="JSON GREP v{version} is utility for filtering selected keys from json string piped from STDOUT".format(version=version))
    parser.add_argument("filter_keys", type=str, nargs="+", help=(
        "List of keys which you want to filter from json dict. "
        "If key is in deeper level of tree structure use '.' separator "
        "to specify how deep is key in dict tree structure. You can also use '*' "
        "at the end of key name to filter keys as 'beginning with'. "
        "You can also specify value of item which you want to pass "
        "only by operator '=' or '~'. '~' means "
        "that value is somewhere in string.")
                        )
    parser.add_argument("-m", "--multiline-output", dest="multiline_output", default=False, action="store_true", help="Use multiline output for filtered result")
    parser.add_argument("-v", "--values_only", dest="values_only", default=False, action="store_true", help="Show only values without keys description")
    parser.add_argument("-l", "--hl", dest="highlight", action="append", help="Highlight case sensitively words in filtered results")
    parser.add_argument("-i", "--ihl", dest="ihighlight", action="append", help="Highlight case insensitively words in filtered results")
    parser.add_argument("-e", "--show-errors", dest="show_errors", default=False, action="store_true", help="Show errors caused by json decode")

    args = parser.parse_args()
    return args


def main():
    signal.signal(signal.SIGINT, _handle_exit)
    args = _handle_args()

    json_filter = JsonFilter(args.filter_keys)
    json_filter.multiline_output = args.multiline_output
    json_filter.values_only = args.values_only
    json_filter.highlight_values = args.highlight
    json_filter.ihighlight_values = args.ihighlight

    for line in sys.stdin:
        try:
            filtered_data = json_filter.filter_keys_and_values(line)
            if filtered_data:
                output = json_filter.format_result(filtered_data)
                sys.stdout.write(output)
        except JsonFilterException as ex:
            if args.show_errors:
                sys.stderr.write("\33[31mJsonFilterException\33[0m: {}\n".format(ex))
    print("DONE.")


if __name__ == '__main__':
    main()
