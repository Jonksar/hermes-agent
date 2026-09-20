"""Deleted sidecar holders remain visible among mixed macOS descriptors."""

import ctypes
import struct

import pytest

import hermes_state_dbfile as dbfile


@pytest.mark.macos_only
def test_finds_deleted_sidecar_holder_among_mixed_descriptors(tmp_path, monkeypatch):
    db_path = tmp_path / "state.db"
    sidecar_path = str(db_path.resolve()) + "-wal"

    class Libproc:
        def proc_listpids(self, kind, typeinfo, buffer, size):
            struct.pack_into("<i", buffer, 0, 123)
            return 4

        def proc_pidinfo(self, pid, flavor, arg, buffer, size):
            # Socket, vnode, pipe. Only the vnode can hold a SQLite sidecar.
            for index, entry in enumerate(((10, 2), (11, 1), (12, 6))):
                struct.pack_into("<iI", buffer, index * 8, *entry)
            return 24

        def proc_pidfdinfo(self, pid, fd, flavor, buffer, size):
            if fd != 11:
                return 0
            # libproc vnode record layout: device, inode, then last pathname.
            struct.pack_into("<I", buffer, 24, 42)
            struct.pack_into("<Q", buffer, 32, 9876543210)
            path = sidecar_path.encode() + b"\0"
            start = 176
            buffer[start:start + len(path)] = path
            return size

    monkeypatch.setattr(dbfile, "_darwin_libproc", Libproc)
    # The buffer protocol suffices; accessing ctypes' .raw would copy the entire
    # fd listing on every iteration and make enumeration quadratic.
    monkeypatch.setattr(ctypes, "create_string_buffer", bytearray)

    assert dbfile.iter_deleted_sqlite_sidecar_holders(db_path) == [(123, sidecar_path)]
