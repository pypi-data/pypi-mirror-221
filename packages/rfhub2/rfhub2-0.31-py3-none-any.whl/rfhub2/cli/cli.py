import click
from pathlib import Path
from typing import Tuple, Union

from rfhub2.cli.api_client import Client
from rfhub2.cli.keywords.keywords_importer import KeywordsImporter
from rfhub2.cli.statistics.statistics_importer import StatisticsImporter


@click.command()
@click.option(
    "-a",
    "--app-url",
    type=click.STRING,
    default="http://localhost:8000",
    help="Specifies IP, URI or host of rfhub2 web application. Default value is http://localhost:8000.",
)
@click.option(
    "-u",
    "--user",
    type=click.STRING,
    default="rfhub",
    help="Specifies rfhub2 user to authenticate on endpoints that requires that. Default value is rfhub.",
)
@click.option(
    "-p",
    "--password",
    type=click.STRING,
    default="rfhub",
    help="Specifies rfhub2 password to authenticate on endpoints that requires that. Default value is rfhub.",
)
@click.option(
    "--no-installed-keywords",
    type=click.BOOL,
    default=False,
    is_flag=True,
    help="Flag specifying if package should skip loading commonly installed libraries, "
    "such as such as BuiltIn, Collections, DateTime etc.",
)
@click.option(
    "--mode",
    "-m",
    type=click.Choice(["keywords", "statistics"], case_sensitive=False),
    default="keywords",
    help="""Choice parameter specifying what kind of data package should add:\n
             - `keywords` - default value, application is working with keywords documentation\n
             - `statistics` - application is working with data about keywords execution.""",
)
@click.option(
    "--load-mode",
    "-l",
    type=click.Choice(["merge", "insert", "append", "update"], case_sensitive=False),
    default="merge",
    help="""Choice parameter specifying in what load mode package should run:\n
             - `merge`  - default value, adds new and updates only matched collections, does nothing with not matched ones\n
             - `insert` - removes all existing collections from app and add ones found in paths\n
             - `append` - adds collections found in paths without removal of existing ones\n
             - `update` - removes collections not found in paths, adds new ones and updates existing ones""",
)
@click.option(
    "--include",
    "-i",
    type=click.STRING,
    default="",
    help="Include all the keywords containing tags matching this pattern. "
    "This option has the same behavior as the --include option of the RobotFramework CLI (with the same format). "
    "By default, all the keywords found are included.",
)
@click.option(
    "--exclude",
    "-e",
    type=click.STRING,
    default="",
    help="Exclude all the keywords containing tags matching this pattern. "
    "This option has the same behavior as the --exclude option of the RobotFramework CLI (with the same format). "
    "By default, no keyword is excluded.",
)
@click.argument("paths", nargs=-1)
def main(
    app_url: str,
    user: str,
    password: str,
    paths: Tuple[Union[Path, str], ...],
    load_mode: str,
    mode: str,
    no_installed_keywords: bool,
    include: str,
    exclude: str,
) -> None:
    """Package to populate rfhub2 with robot framework keywords
       from libraries and resource files."""
    client = Client(app_url, user, password)
    if mode == "keywords":
        rfhub_importer = KeywordsImporter(
            client, paths, no_installed_keywords, load_mode, include, exclude
        )
        loaded_collections, loaded_keywords = rfhub_importer.import_data()
        print(
            f"\nSuccessfully loaded {loaded_collections} collections with {loaded_keywords} keywords."
        )
    elif mode == "statistics":
        rfhub_importer = StatisticsImporter(client, paths)
        loaded_files, loaded_statistics = rfhub_importer.import_data()
        print(
            f"\nSuccessfully loaded {loaded_files} files with {loaded_statistics} statistics."
        )
