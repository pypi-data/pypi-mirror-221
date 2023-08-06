#! /usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2021-current alexpdev
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##############################################################################
"""
Testing the edit torrent feature.
"""

import sys

import pyben
import pytest

from tests import dir1, dir2, metafile2
from torrentfile.cli import main
from torrentfile.edit import edit_torrent


def test_fix():
    """
    Testing dir fixtures.
    """
    assert dir2 and metafile2 and dir1


@pytest.mark.parametrize(
    "announce", [["urla"], ["urlb", "urlc"], ["urla", "urlb", "urlc"]])
def test_edit_torrent(metafile2, announce):
    """
    Test edit torrent with announce param.
    """
    edits = {"announce": announce}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["announce-list"] == [announce]


@pytest.mark.parametrize("announce", ["urla", "urlb urlc", "urla urlb urlc"])
def test_edit_torrent_str(metafile2, announce):
    """
    Test edit torrent with announce param as string.
    """
    edits = {"announce": announce}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["announce-list"] == [announce.split()]


@pytest.mark.parametrize("url_list", ["urla", "urlb urlc", "urla urlb urlc"])
def test_edit_urllist_str(metafile2, url_list):
    """
    Test edit torrent with webseed param.
    """
    edits = {"url-list": url_list}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["url-list"] == url_list.split()


@pytest.mark.parametrize("httpseeds", ["urla", "urlb urlc", "urla urlb urlc"])
def test_edit_httpseeds_str(metafile2, httpseeds):
    """
    Test edit torrent with webseed param.
    """
    edits = {"httpseeds": httpseeds}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["httpseeds"] == httpseeds.split()


@pytest.mark.parametrize(
    "url_list", [["urla"], ["urlb", "urlc"], ["urla", "urlb", "urlc"]])
def test_edit_urllist(metafile2, url_list):
    """
    Test edit torrent with webseed param as string.
    """
    edits = {"url-list": url_list}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["url-list"] == url_list


@pytest.mark.parametrize(
    "httpseed", [["urla"], ["urlb", "urlc"], ["urla", "urlb", "urlc"]])
def test_edit_httpseeds(metafile2, httpseed):
    """
    Test edit torrent with webseed param as string.
    """
    edits = {"httpseeds": httpseed}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["httpseeds"] == httpseed


@pytest.mark.parametrize("comment", ["COMMENT", "COMIT", "MITCO"])
def test_edit_comment(metafile2, comment):
    """
    Test edit torrent with comment param.
    """
    edits = {"comment": comment}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["info"]["comment"] == comment


@pytest.mark.parametrize("source", ["SomeSource", "NoSouce", "MidSource"])
def test_edit_source(metafile2, source):
    """
    Test edit torrent with source param.
    """
    edits = {"source": source}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["info"]["source"] == source


def test_edit_private_true(metafile2):
    """
    Test edit torrent with private param.
    """
    edits = {"private": "1"}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert data["info"]["private"] == 1


def test_edit_private_false(metafile2):
    """
    Test edit torrent with private param False.
    """
    edits = {"private": ""}
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta
    assert "private" not in data["info"]


def test_edit_none(metafile2):
    """
    Test edit torrent with None for all params.
    """
    edits = {
        "announce": None,
        "url-list": None,
        "comment": None,
        "source": None,
        "private": None,
    }
    data = pyben.load(metafile2)
    edited = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta == edited


def test_edit_removal(metafile2):
    """
    Test edit torrent with empty for all params.
    """
    edits = {
        "announce": "",
        "url-list": "",
        "httpseeds": "",
        "comment": "",
        "source": "",
        "private": "",
    }
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    assert data == meta


@pytest.mark.parametrize("comment", ["commenta", "commentb", "commentc"])
@pytest.mark.parametrize("source", ["sourcea", "sourceb", "sourcec"])
@pytest.mark.parametrize("announce", [["url1", "url2", "url3"], ["url1"]])
@pytest.mark.parametrize("webseed", [["ftp1"], ["ftpa", "ftpb"]])
@pytest.mark.parametrize("httpseed", [["ftp1"], ["ftpa", "ftpb"]])
def test_edit_cli(metafile2, comment, source, announce, webseed, httpseed):
    """
    Test edit torrent with all params on cli.
    """
    sys.argv = [
        "torrentfile",
        "edit",
        metafile2,
        "--comment",
        comment,
        "--source",
        source,
        "--web-seed",
        webseed,
        "--http-seed",
        httpseed,
        "--tracker",
        announce,
        "--private",
    ]
    main()
    meta = pyben.load(metafile2)
    info = meta["info"]
    assert comment == info.get("comment")
    assert source == info.get("source")
    assert info.get("private") == 1
    assert meta["announce-list"] == [[announce]]
    assert meta["url-list"] == [webseed]


def test_metafile_edit_with_unicode(metafile2):
    """
    Test if editing full unicode works as it should.
    """
    edits = {
        "comment": "丂七万丈三与丏丑丒专且丕世丗両丢丣两严丩个丫丬中丮丯.torrent",
        "source": "丂七万丏丑严丩个丫丬中丮丯",
    }
    data = edit_torrent(metafile2, edits)
    meta = pyben.load(metafile2)
    com1 = data["info"]["comment"]
    com2 = meta["info"]["comment"]
    msg = edits["comment"]
    assert com1 == com2 == msg
