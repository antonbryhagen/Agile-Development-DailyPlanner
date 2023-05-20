#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run the app.

"""

from planner import interface


def main():
    """Execute the main program."""
    u_i = interface.Interface()
    u_i.display_menu()


if __name__ == "__main__":
    main()
