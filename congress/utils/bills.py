import re

from congress.utils.utils import data_dir


def split_bill_id(bill_id):
    return re.match("^([a-z]+)(\d+)-(\d+)$", bill_id).groups()


def build_bill_id(bill_type, bill_number, congress):
    return "%s%s-%s" % (bill_type, bill_number, congress)


def split_bill_version_id(bill_version_id):
    return re.match("^([a-z]+)(\d+)-(\d+)-([a-z\d]+)$", bill_version_id).groups()


def extract_bills(text, session):
    bill_ids = []

    p = re.compile(
        "((S\.|H\.)(\s?J\.|\s?R\.|\s?Con\.| ?)(\s?Res\.)*\s?\d+)", flags=re.IGNORECASE
    )
    bill_matches = p.findall(text)

    if bill_matches:
        for b in bill_matches:
            bill_text = "%s-%s" % (
                b[0].lower().replace(" ", "").replace(".", "").replace("con", "c"),
                session,
            )
            if bill_text not in bill_ids:
                bill_ids.append(bill_text)

    return bill_ids


def output_for_bill(bill_id, format, is_data_dot=True):
    bill_type, number, congress = split_bill_id(bill_id)
    if is_data_dot:
        fn = "data.%s" % format
    else:
        fn = format
    return "%s/%s/bills/%s/%s%s/%s" % (
        data_dir(),
        congress,
        bill_type,
        bill_type,
        number,
        fn,
    )
