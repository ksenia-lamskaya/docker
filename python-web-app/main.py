#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def main():
    database_url = os.environ["DATABASE_URL"]
    print(database_url)


if __name__ == "__main__":
    main()
    