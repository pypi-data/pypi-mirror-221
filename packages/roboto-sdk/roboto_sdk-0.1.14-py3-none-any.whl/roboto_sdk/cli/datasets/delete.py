#  Copyright (c) 2023 Roboto Technologies, Inc.
import argparse

from ...domain.datasets import Dataset
from ..command import RobotoCommand
from ..common_args import add_org_arg
from ..context import CLIContext
from .shared_helpdoc import DATASET_ID_HELP


def delete(args, context: CLIContext, parser: argparse.ArgumentParser):
    dataset = Dataset.from_id(
        dataset_delegate=context.datasets, dataset_id=args.dataset_id, org_id=args.org
    )
    dataset.delete()
    print(f"Deleted dataset {args.dataset_id}")


def delete_setup_parser(parser):
    parser.add_argument(
        "-d", "--dataset-id", type=str, required=True, help=DATASET_ID_HELP
    )
    add_org_arg(parser)


delete_command = RobotoCommand(
    name="delete",
    logic=delete,
    setup_parser=delete_setup_parser,
    command_kwargs={"help": "Delete dataset (and all related subresources) by id."},
)
