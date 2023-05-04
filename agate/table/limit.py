#!/usr/bin/env python
# pylint: disable=W0212


def limit(self, start_or_stop=None, stop=None, step=None):
    """
    Create a new table with fewer rows.

    See also: Python's builtin :func:`slice`.

    :param start_or_stop:
        If the only argument, then how many rows to include, otherwise,
        the index of the first row to include.
    :param stop:
        The index of the last row to include.
    :param step:
        The size of the jump between rows to include. (`step=2` will return
        every other row.)
    :returns:
        A new :class:`.Table`.
    """
    s = slice(start_or_stop, stop, step) if stop or step else slice(start_or_stop)
    rows = self._rows[s]

    row_names = self._row_names[s] if self._row_names is not None else None
    return self._fork(rows, row_names=row_names)
