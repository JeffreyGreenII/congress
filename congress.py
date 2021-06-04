import click

from congress.tasks import (
    bills,
    committee_meetings,
    govinfo,
    nomination_info,
    nominations,
    votes,
)


@click.group()
def cli():
    """
    Command-line interface for the congress library.
    """


@cli.command()
@click.option("--bill_id", required=True, help="ID of the bill.")
@click.option("--custom_fetch_function", default=None)
def get_bill(bill_id, custom_fetch_function):
    """Get bill by ID."""
    bills.run({"bill_id": bill_id, "reparse_actions": custom_fetch_function})


@cli.command()
@click.option("--limit", default=None, help="Limit number of votes returned.")
@click.option("--custom_fetch_function", default=None)
def get_bills(limit, custom_fetch_function):
    """Get votes."""
    bills.run({"limit": limit, "reparse_actions": custom_fetch_function})


@cli.command()
@click.option(
    "--chamber",
    default=None,
    help="Filters votes based on congressional chamber.",
    type=click.Choice(["House", "Senate"], case_sensitive=False),
)
@click.option(
    "--load_by",
    default=None,
    help="Takes a range of House Event IDs. Requires beginning and end IDs with a dash between, otherwise, loads by the committee feeds.",
)
@click.option(
    "--docs",
    is_flag=True,
    help="If provided, it will download House committee documents and convert them into text documents.",
)
def get_committee_meetings(chamber, load_by, docs):
    """Get committee meeting documents."""
    committee_meetings.run(
        {
            "chamber": chamber,
            "load_by": load_by,
            "docs": not docs,
        }
    )


@cli.command()
@click.option(
    "--years",
    default="",
    help="Comma-separated list of years to download from. Applies to collections that are divided by year.",
)
@click.option(
    "--congress",
    default="",
    help="Comma-separated list of congresses to download from. Applies to bulk data collections like BILLSTATUS that are grouped by Congress + Bill Type.",
)
@click.option(
    "--extract",
    help="Extract the MODS, PDF, text, XML, or PREMIS file associated with each package from the downloaded package ZIP file.",
    type=click.Choice(["mods", "pdf", "text", "xml", "premis"], case_sensitive=False),
)
@click.option(
    "--filter",
    help="Only stores files that match the regex. Regular collections are matched against the package name (i.e. BILLS-113hconres66ih) while bulk data items are matched against the their file path (i.e. 113/1/hconres/BILLS-113hconres66ih.xml)..",
    type=click.Choice(["mods", "pdf", "text", "xml", "premis"], case_sensitive=False),
)
def get_gov_info(years, congress, extract, filter):
    """Downloads documents from GPO's GovInfo.gov site."""
    govinfo.run(
        {"years": years, "congress": congress, "extract": extract, "filter": filter}
    )


@cli.command()
@click.option("--nomination_id", required=True, help="ID of the nomination.")
def get_nomination_info(nomination_id):
    """Get nomination info by ID."""
    nomination_info.run({"nomination_id": nomination_id})


@cli.command()
@click.option("--nomination_id", required=True, help="ID of the nomination.")
def get_nomination_by_id(nomination_id):
    """Get nomination by ID."""
    nominations.run({"nomination_id": nomination_id})


@cli.command()
@click.option(
    "--congress",
    required=True,
    help="Comma-separated list of congresses to download from.",
)
@click.option("--limit", default=None, help="Limit number of nominations returned.")
def get_nominations(congress, limit):
    """Get nominations."""
    nominations.run({"congress": congress, "limit": limit})


@cli.command()
@click.option("--vote_id", required=True, help="ID of the vote.")
def get_vote(vote_id):
    """Get vote by ID."""
    votes.run({"vote_id": vote_id})


@cli.command()
@click.option(
    "--session",
    default=None,
    help="Filters votes based on congressional session (ex. 116, 117).",
)
@click.option(
    "--chamber",
    default=None,
    help="Filters votes based on congressional chamber.",
    type=click.Choice(["House", "Senate"], case_sensitive=False),
)
@click.option("--limit", default=None, help="Limit number of votes returned.")
def get_votes(session, chamber, limit):
    """Get bills."""
    votes.run(
        {
            "limit": limit,
            "chamber": chamber,
            "congress": True if session is not None else False,
            "session": session,
        }
    )


if __name__ == "__main__":
    cli()
