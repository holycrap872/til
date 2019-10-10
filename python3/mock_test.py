#!/usr/bin/env python3

## GT_EXTERNAL_LEGEND

import os
import typing
import tempfile
import shutil
import logging
from unittest.mock import patch, mock_open, call, Mock

##
## `python3 -m pytest mock_test.py`
##

class TestObject:

    def __init__(self) -> None:
        pass


    def get_next_char(self) -> str:
        return 'a'


    def get_next_char_iter(self) -> typing.Iterable[str]:
        return iter('a', 'b', 'c')


def test_constant_return_1() -> None:
    """
    """
    output_dir = tempfile.mkdtemp(dir=".", suffix="_banner_grab_gatherer_test")
    output_dir = os.path.join(os.getcwd(), output_dir)

    try:
        to = TestObject()
        with patch.object(to, 'get_next_char') as p:
            p.return_value = 'b'

            assert to.get_next_char() == 'b'
            assert to.get_next_char() == 'b'
            assert to.get_next_char() == 'b'


    finally:
        shutil.rmtree(output_dir)



def test_changing_return_1() -> None:
    """
    """
    output_dir = tempfile.mkdtemp(dir=".", suffix="_banner_grab_gatherer_test")
    output_dir = os.path.join(os.getcwd(), output_dir)

    try:
        to = TestObject()
        with patch.object(to, 'get_next_char') as p:
            p.side_effect = [ 'b', 'b', 'a', 'b' ]

            assert to.get_next_char() == 'b'
            assert to.get_next_char() == 'b'
            assert to.get_next_char() == 'a'
            assert to.get_next_char() == 'b'

            assertion_raised = False
            try:
                to.get_next_char()
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True


    finally:
        shutil.rmtree(output_dir)


def test_constant_return_iter_1() -> None:
    """
    """
    output_dir = tempfile.mkdtemp(dir=".", suffix="_banner_grab_gatherer_test")
    output_dir = os.path.join(os.getcwd(), output_dir)

    try:
        to = TestObject()
        with patch.object(to, 'get_next_char_iter') as p:

            ##
            ## THIS DOESN't WORK AS YOU'D EXPECT
            ##
            p.return_value = iter([ 'b', 'b' ])


            ## Try once
            next_ite = to.get_next_char_iter()
            assert next(next_ite) == 'b'
            assert next(next_ite) == 'b'

            assertion_raised = False
            try:
                next(next_ite)
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True


            ## Try again
            next_ite2 = to.get_next_char_iter()
            assert next(next_ite2) == 'b'
            assert next(next_ite2) == 'b'

            assertion_raised = False
            try:
                next(next_ite)
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True


    finally:
        shutil.rmtree(output_dir)


def test_changing_return_changing_iter_1() -> None:
    """
    """
    output_dir = tempfile.mkdtemp(dir=".", suffix="_banner_grab_gatherer_test")
    output_dir = os.path.join(os.getcwd(), output_dir)

    try:
        to = TestObject()
        with patch.object(to, 'get_next_char_iter') as p:
            p.side_effect = [ iter([ 'b', 'b' ]), iter([ 'a', 'b' ]) ]

            ## Try once
            next_ite = to.get_next_char_iter()
            assert next(next_ite) == 'b'
            assert next(next_ite) == 'b'

            assertion_raised = False
            try:
                next(next_ite)
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True


            ## Try again
            next_ite = to.get_next_char_iter()
            assert next(next_ite) == 'a'
            assert next(next_ite) == 'b'

            assertion_raised = False
            try:
                next(next_ite)
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True


            ## Try third time
            assertion_raised = False
            try:
                to.get_next_char_iter()
            except StopIteration:
                assertion_raised = True
            assert assertion_raised == True

    finally:
        shutil.rmtree(output_dir)
