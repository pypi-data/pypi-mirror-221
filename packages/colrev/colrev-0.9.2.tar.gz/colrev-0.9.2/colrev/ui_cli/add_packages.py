#!/usr/bin/env python3
"""Scripts to add packages using the cli."""
from __future__ import annotations

from pathlib import Path

import requests

import colrev.env.package_manager
import colrev.ops.built_in.data.bibliography_export
import colrev.ui_cli.cli_colors as colors
import colrev.ui_cli.cli_load


def add_search_source(
    *,
    search_operation: colrev.ops.search.Search,
    query: str,
) -> None:
    """Add a search source package_endpoint"""

    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches

    if Path(query).is_file():
        # pylint: disable=import-outside-toplevel
        import shutil

        filename = search_operation.get_unique_filename(
            file_path_string=Path(query).name
        )
        dst = search_operation.review_manager.search_dir / Path(filename).name
        shutil.copyfile(query, dst)
        search_operation.review_manager.logger.info(f"Copied {filename} to repo.")
        load_operation = search_operation.review_manager.get_load_operation()

        heuristic_list = load_operation.get_new_sources_heuristic_list()
        new_sources = colrev.ui_cli.cli_load.select_new_source(
            heuristic_result_list=heuristic_list, skip_query=True
        )

        load_operation.main(new_sources=new_sources)
        # Note : load runs the heuristics.
        return

    if ":" in query:
        package_identifier = query[: query.find(":")]
        query = query[query.find(":") + 1 :]
    else:
        package_identifier = query
        query = ""

    package_manager = search_operation.review_manager.get_package_manager()

    search_source = package_manager.load_packages(
        package_type=colrev.env.package_manager.PackageEndpointType.search_source,
        selected_packages=[{"endpoint": package_identifier}],
        operation=search_operation,
        instantiate_objects=False,
    )
    s_obj = search_source[package_identifier]
    add_source = s_obj.add_endpoint(search_operation, query)  # type: ignore
    search_operation.add_source(add_source=add_source)


def add_prep(
    *,
    prep_operation: colrev.ops.prep.Prep,
    query: str,
) -> None:
    """Add a prep package_endpoint"""

    package_identifier = query

    prep_operation.review_manager.logger.info(
        f"{colors.GREEN}Add prep package:{colors.END} {package_identifier}"
    )
    prep_operation.review_manager.settings.prep.prep_rounds[
        0
    ].prep_package_endpoints.append({"endpoint": package_identifier})
    prep_operation.review_manager.save_settings()

    prep_operation.review_manager.create_commit(
        msg=f"Add prep {package_identifier}",
    )


def add_prescreen(
    *,
    prescreen_operation: colrev.ops.prescreen.Prescreen,
    add: str,
) -> None:
    """Add a prescreen package_endpoint"""

    package_identifier, params_str = add.split(":")
    package_identifier = package_identifier.lower()
    params = {}
    for p_el in params_str.split(";"):
        key, value = p_el.split("=")
        params[key] = value

    p_dict = {**{"endpoint": package_identifier}, **params}
    package_manager = prescreen_operation.review_manager.get_package_manager()
    endpoint_dict = package_manager.load_packages(
        package_type=colrev.env.package_manager.PackageEndpointType.prescreen,
        selected_packages=[p_dict],
        operation=prescreen_operation,
    )
    prescreen_operation.review_manager.logger.info(
        f"{colors.GREEN}Add prescreen endpoint{colors.END}"
    )

    if not hasattr(endpoint_dict[package_identifier], "add_endpoint"):
        prescreen_operation.review_manager.logger.info(
            'Cannot add endpoint (mising "add_endpoint" method)'
        )
        return

    endpoint_dict[package_identifier].add_endpoint(params=params)  # type: ignore
    prescreen_operation.review_manager.save_settings()
    prescreen_operation.review_manager.create_commit(
        msg=f"Add prescreen endpoint ({package_identifier})",
    )


def __extend_data_short_forms(*, add: str) -> str:
    # pylint: disable=too-many-return-statements
    if add == "endnote":
        return "colrev.bibliography_export:bib_format=endnote"
    if add == "zotero":
        return "colrev.bibliography_export:bib_format=zotero"
    if add == "jabref":
        return "colrev.bibliography_export:bib_format=jabref"
    if add == "mendeley":
        return "colrev.bibliography_export:bib_format=mendeley"
    if add == "citavi":
        return "colrev.bibliography_export:bib_format=citavi"
    if add == "rdf_bibliontology":
        return "colrev.bibliography_export:bib_format=rdf_bibliontology"
    return add


def add_data(
    *,
    data_operation: colrev.ops.data.Data,
    add: str,
) -> None:
    """Add a data package_endpoint"""

    # pylint: disable=too-many-locals

    package_manager = data_operation.review_manager.get_package_manager()
    available_data_endpoints = package_manager.discover_packages(
        package_type=colrev.env.package_manager.PackageEndpointType.data
    )
    add = __extend_data_short_forms(add=add)
    add, params = add.split(":")
    data_operation.review_manager.logger.info(f"Add {add} data endpoint")
    if add in available_data_endpoints:
        package_endpoints = package_manager.load_packages(
            package_type=colrev.env.package_manager.PackageEndpointType.data,
            selected_packages=[{"endpoint": add}],
            operation=data_operation,
        )
        endpoint = package_endpoints[add]

        default_endpoint_conf = endpoint.get_default_setup()  # type: ignore
        for item in params.split(";"):
            key, value = item.split("=")
            default_endpoint_conf[key] = value

        if add == "colrev.paper_md":
            if input("Select a custom word template (y/n)?") == "y":
                template_name = input(
                    'Please copy the word template to " \
                "the project directory and enter the filename.'
                )
                default_endpoint_conf["word_template"] = template_name
            else:
                print("Adding APA as a default")

            if input("Select a custom citation stlye (y/n)?") == "y":
                print(
                    "Citation stlyes are available at: \n"
                    "https://github.com/citation-style-language/styles"
                )
                csl_link = input("Please select a citation style and provide the link.")
                ret = requests.get(csl_link, allow_redirects=True, timeout=30)
                with open(Path(csl_link).name, "wb") as file:
                    file.write(ret.content)
            else:
                print("Adding APA as a default")

            data_operation.review_manager.dataset.add_changes(
                path=Path(Path(csl_link).name)
            )
            data_operation.review_manager.dataset.add_changes(
                path=default_endpoint_conf["word_template"]
            )

        data_operation.add_data_endpoint(data_endpoint=default_endpoint_conf)
        data_operation.review_manager.create_commit(
            msg="Add data endpoint",
            script_call="colrev data",
        )

    else:
        print("Data format not available")
        return

    # Note : reload updated settings
    review_manager = colrev.review_manager.ReviewManager(force_mode=True)
    data_operation = colrev.ops.data.Data(review_manager=review_manager)

    data_operation.main(selection_list=["colrev.bibliography_export"], silent_mode=True)
    data_operation.review_manager.logger.info(
        f"{colors.GREEN}Successfully added {add} data endpoint{colors.END}"
    )
