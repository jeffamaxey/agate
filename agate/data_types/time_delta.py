#!/usr/bin/env python

import datetime

import pytimeparse
import six

from agate.data_types.base import DataType
from agate.exceptions import CastError


class TimeDelta(DataType):
    """
    Data representing the interval between two dates and/or times.
    """
    def cast(self, d):
        """
        Cast a single value to :class:`datetime.timedelta`.

        :param d:
            A value to cast.
        :returns:
            :class:`datetime.timedelta` or :code:`None`
        """
        if isinstance(d, datetime.timedelta) or d is None:
            return d
        elif isinstance(d, six.string_types):
            d = d.strip()

            if d.lower() in self.null_values:
                return None
        else:
            raise CastError(f'Can not parse value "{d}" as timedelta.')

        try:
            seconds = pytimeparse.parse(d)
        except AttributeError:
            seconds = None

        if seconds is None:
            raise CastError(f'Can not parse value "{d}" to as timedelta.')

        return datetime.timedelta(seconds=seconds)
