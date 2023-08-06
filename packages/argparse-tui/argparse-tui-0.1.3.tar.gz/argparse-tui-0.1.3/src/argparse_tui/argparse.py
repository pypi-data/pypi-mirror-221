from __future__ import annotations

import argparse
import sys
from typing import Any

from .constants import DEFAULT_COMMAND_NAME
from .schemas import ArgumentSchema, CommandName, CommandSchema, OptionSchema
from .tui import Tui


def introspect_argparse_parser(
    parser: argparse.ArgumentParser,
    cmd_ignorelist: list[argparse.ArgumentParser] | None = None,
) -> dict[CommandName, CommandSchema]:
    def process_command(
        cmd_name: CommandName,
        parser: argparse.ArgumentParser,
        parent=None,
    ) -> CommandSchema:
        cmd_data = CommandSchema(
            name=cmd_name,
            docstring=parser.description,
            options=[],
            arguments=[],
            subcommands={},
            parent=parent,
        )

        # this is specific to yapx.
        param_types: dict[str, type[Any]] | None = getattr(parser, "_dest_type", None)

        for param in parser._actions:
            if isinstance(param, TuiAction) or argparse.SUPPRESS in [
                param.help,
                param.default,
            ]:
                continue

            if isinstance(param, argparse._SubParsersAction):
                for subparser_name, subparser in param.choices.items():
                    if subparser.description != argparse.SUPPRESS and (
                        not cmd_ignorelist or subparser not in cmd_ignorelist
                    ):
                        cmd_data.subcommands[
                            CommandName(subparser_name)
                        ] = process_command(
                            CommandName(subparser_name),
                            subparser,
                            parent=cmd_data,
                        )
                continue

            param_type: type[Any] | None = None
            if param_types:
                param_type = param_types.get(param.dest, param.type)

            if param_type is None and param.default is not None:
                param_type = type(param.default)

            is_counting: bool = False
            is_multiple: bool = False
            is_flag: bool = False

            opts: list[str] = param.option_strings
            secondary_opts: list[str] = []

            if isinstance(param, argparse._CountAction):
                is_counting = True
            elif isinstance(param, argparse._AppendAction):
                is_multiple = True
            elif isinstance(param, argparse._StoreConstAction):
                is_flag = True
            elif (
                sys.version_info >= (3, 9)
                and isinstance(param, argparse.BooleanOptionalAction)
            ) or type(param).__name__ == "BooleanOptionalAction":
                # check the type by name, because 'BooleanOptionalAction'
                # is often manually backported to Python versions < 3.9.
                if param_type is None:
                    param_type = bool
                is_flag = True

                if hasattr(param, "_negation_option_strings"):
                    # this is specific to `yapx`
                    secondary_opts = param._negation_option_strings
                    opts = [x for x in param.option_strings if x not in secondary_opts]
                else:
                    secondary_prefix: str = "--no-"
                    opts = [
                        x
                        for x in param.option_strings
                        if not x.startswith(secondary_prefix)
                    ]
                    secondary_opts = [x for x in param.option_strings if x not in opts]

            # look for these "tags" in the help text: "secret", "prompt"
            # if present, set variables and remove from the help text.
            is_secret: bool = False
            is_prompt: bool = False
            param_help: str = param.help
            if param_help:
                param_help = param_help.replace("%(default)s", str(param.default))

                tag_prefix: str = "<"
                tag_suffix: str = ">"
                tag_start: int = param_help.find(tag_prefix)
                if tag_start >= 0:
                    tag_end: int = param_help.find(tag_suffix)
                    if tag_end > tag_start:
                        tag_txt: str = param_help[tag_start : tag_end + 1]
                        tags: list[str] = [x.strip() for x in tag_txt[1:-1].split(",")]
                        is_secret = "secret" in tags
                        is_prompt = "prompt" in tags
                        if any([is_secret, is_prompt]):
                            param_help = param_help.replace(tag_txt, "")

            nargs: int = (
                1
                if param.nargs in [None, "?"]
                else -1
                if param.nargs in ["+", "*", argparse.REMAINDER]
                else int(param.nargs)
            )
            multi_value: bool = nargs < 0 or nargs > 1

            if param.option_strings:
                option_data = OptionSchema(
                    name=opts,
                    type=param_type,
                    is_flag=is_flag,
                    counting=is_counting,
                    secondary_opts=secondary_opts,
                    required=param.required,
                    default=param.default,
                    help=param_help,
                    choices=param.choices,
                    multiple=is_multiple,
                    multi_value=multi_value,
                    nargs=nargs,
                    secret=is_secret,
                    read_only=is_prompt,
                    placeholder="< You will be prompted. >" if is_prompt else "",
                )
                cmd_data.options.append(option_data)

            else:
                argument_data = ArgumentSchema(
                    name=param.dest,
                    type=param_type,
                    required=param.required,
                    default=param.default,
                    help=param_help,
                    choices=param.choices,
                    multiple=is_multiple,
                    multi_value=multi_value,
                    nargs=nargs,
                    secret=is_secret,
                    read_only=is_prompt,
                    placeholder="< You will be prompted. >" if is_prompt else "",
                )
                cmd_data.arguments.append(argument_data)

        return cmd_data

    data: dict[CommandName, CommandSchema] = {}

    root_cmd_name = CommandName("root")
    data[root_cmd_name] = process_command(root_cmd_name, parser)

    return data


def invoke_tui(
    parser: argparse.ArgumentParser,
    cmd_ignorelist: list[argparse.ArgumentParser] = None,
    command_filter: str | None = None,
):
    """
    Examples:
        >>> import argparse
        >>> from argparse_tui import invoke_tui
        ...
        >>> parser = argparse.ArgumentParser(prog="awesome-app")
        >>> _ = parser.add_argument("--value")
        ...
        >>> invoke_tui(parser)  # doctest: +SKIP
    """

    if cmd_ignorelist is None:
        cmd_ignorelist = [parser]

    Tui(
        introspect_argparse_parser(parser, cmd_ignorelist=cmd_ignorelist),
        app_name=parser.prog,
        command_filter=command_filter,
    ).run()


class TuiAction(argparse.Action):
    """argparse `Action` that will analyze the parser and display a TUI.

    Examples:
        >>> import argparse
        >>> from argparse_tui import TuiAction
        ...
        >>> parser = argparse.ArgumentParser()
        >>> _ = parser.add_argument('--tui', action=TuiAction)
        ...
        >>> parser.print_usage()
        usage: __main__.py [-h] [--tui [TUI]]
    """

    def __init__(
        self,
        option_strings: list[str],
        dest: str = argparse.SUPPRESS,
        default: Any = argparse.SUPPRESS,
        help: str | None = "Open Textual UI.",
        const: str = None,
        metavar: str = None,
        nargs: int | str | None = None,
        **_kwargs: Any,
    ):
        super(TuiAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs="?" if nargs is None else nargs,
            help=help,
            const=const,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        root_parser: argparse.ArgumentParser = getattr(
            namespace,
            "_parent_parser",
            parser,
        )

        invoke_tui(root_parser, cmd_ignorelist=[parser], command_filter=values)

        parser.exit()


def add_tui_argument(
    parser: argparse.ArgumentParser,
    option_strings: str | list[str] = None,
    help: str = "Open Textual UI.",
    default=argparse.SUPPRESS,
    **kwargs,
) -> None:
    """

    Args:
        parser: the argparse parser
        option_strings: list of CLI flags that will invoke the TUI (default=`--tui`)
        help: help message for the argument

    Examples:
        >>> import argparse
        >>> from argparse_tui import add_tui_argument
        ...
        >>> parser = argparse.ArgumentParser()
        ...
        >>> add_tui_argument(parser)
        ...
        >>> parser.print_usage()
        usage: __main__.py [-h] [--tui [CMD]]
    """
    if not option_strings:
        option_strings = [f"--{DEFAULT_COMMAND_NAME.replace('_', '-').lstrip('-')}"]
    elif isinstance(option_strings, str):
        option_strings = [option_strings]

    parser.add_argument(
        *option_strings,
        metavar="CMD",
        action=TuiAction,
        default=default,
        help=help,
        **kwargs,
    )


def add_tui_command(
    parser: argparse.ArgumentParser,
    command: str = DEFAULT_COMMAND_NAME,
    help: str = "Open Textual UI.",
    **kwargs: Any,
) -> argparse._SubParsersAction:
    """

    Args:
        parser: the argparse parser
        command: name of the CLI command that will invoke the TUI (default=`tui`)
        help: help message for the argument
        **kwargs: if subparsers do not already exist, create with these kwargs.

    Examples:
        >>> import argparse
        >>> from argparse_tui import add_tui_argument
        ...
        >>> parser = argparse.ArgumentParser()
        >>> subparsers = parser.add_subparsers()
        ...
        >>> _ = add_tui_command(parser)
        ...
        >>> parser.print_usage()
        usage: __main__.py [-h] {tui} ...
    """

    subparsers: argparse._SubParsersAction
    if parser._subparsers is None:
        subparsers = parser.add_subparsers(**kwargs)
    else:
        for action in parser._actions:
            if isinstance(action, argparse._SubParsersAction):
                subparsers = action
                break

    tui_parser = subparsers.add_parser(
        command,
        description=argparse.SUPPRESS,
        help=help,
    )
    tui_parser.set_defaults(_parent_parser=parser)

    add_tui_argument(
        tui_parser,
        option_strings=["cmd_filter"],
        default=None,
        help="Command filter",
    )

    return subparsers
