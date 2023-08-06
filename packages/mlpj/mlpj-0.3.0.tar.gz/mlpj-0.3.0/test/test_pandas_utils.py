"""
Unit tests for `mlpj.pandas_utils`.
"""
import datetime
import collections
import io
from typing import List

import numpy as np
import pandas as pd
import numba
import pandas.testing as pd_testing
import pytest

from mlpj import python_utils as pu
from mlpj import pandas_utils as pdu

nan = np.nan


def test_from_items() -> None:
    pd_testing.assert_frame_equal(
        pdu.from_items([
            ('b', np.array([3, 8])),
            ('a', ['first', 'second']),
        ], index=[3, 4]),
        pd.DataFrame([[3, 'first'], [8, 'second']],
                     columns=['b', 'a'], index=[3, 4]))

    df = pdu.from_items([
        ('b', np.array([3, 8])),
        ('a', ['first', 'second']),
    ])
    pd_testing.assert_frame_equal(
        df,
        pd.DataFrame([[3, 'first'], [8, 'second']],
                     columns=['b', 'a']))
    assert df.a.dtype == np.dtype('O')
    assert df.b.dtype == np.dtype('int64')

    with pytest.raises(ValueError):
        pdu.from_items([
            ('b', np.array([3, 8, 9])),
            ('a', ['first', 'second']),
        ], index=[3, 4])


def test_wide_display() -> None:
    out = io.StringIO()
    with pdu.wide_display():
        n_cols = 50
        df = pd.DataFrame(np.random.randint(low=0, high=3, size=(2, n_cols)),
                          columns=np.arange(n_cols))
        print(df, file=out)
    lines = out.getvalue().splitlines()
    assert len(lines) == 3


def test_is_numerical() -> None:
    assert pdu.is_numerical(pd.Series([3, 4]))
    assert pdu.is_numerical(pd.Series([3.5, 4]))
    assert pdu.is_numerical(pd.Series([True, False]))
    assert pdu.is_numerical(pd.Series([3.5, 4, nan]))
    assert not pdu.is_numerical(pd.Series(["foo", "bar"]))


def test_get_colnames() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'b', 'a']),
        ('c', ['x', 'y', 'z', 'x'])
    ])
    np.testing.assert_array_equal(pdu.get_colnames(df), ['a', 'b', 'c'])

    dfg = df.groupby('b')
    np.testing.assert_array_equal(pdu.get_colnames(dfg), ['a', 'b', 'c'])

    np.testing.assert_array_equal(pdu.get_colnames(['x', 'y']), ['x', 'y'])


def test_all_colnames_except() -> None:
    X = pd.DataFrame(np.eye(4), columns=['x', 'a', 'ba', 'c'])
    assert pdu.all_colnames_except(X, ['a', 'c']) == ['x', 'ba']

    X = pd.DataFrame(np.eye(4), columns=list('abcd'))
    assert pdu.all_colnames_except(X, ['c', 'a']) == ['b', 'd']
    assert pdu.all_colnames_except(X, ['c', 'a', 'b', 'd']) == []


def test_category_colnames() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'b', 'a']),
        ('c', ['x', 'y', 'z', 'x'])
    ])

    assert pdu.category_colnames(df) == []
    for colname in ['a', 'b']:
        df[colname] = df[colname].astype('category')
    assert pdu.category_colnames(df) == ['a', 'b']

    assert pdu.category_colnames(df, feature_list=('b', 'c')) == ['b']


def test_rename_column() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'b', 'a']),
    ])

    pdu.rename_column(df, 'b', 'b1')
    pd_testing.assert_frame_equal(
        df,
        pdu.from_items([
            ('a', [3, 4, 3, 2]),
            ('b1', ['a', 'b', 'b', 'a']),
        ]))

    with pytest.raises(KeyError):
        pdu.rename_column(df, 'foo', 'bar')


def test_drop_index() -> None:
    df = pdu.from_items([
        ('b', np.array([3, 8])),
        ('a', ['first', 'second']),
    ], index=[3, 4])

    pdu.drop_index(df)

    pd_testing.assert_frame_equal(
        df,
        pdu.from_items([
            ('b', np.array([3, 8])),
            ('a', ['first', 'second'])
        ]))


def test_drop_columns() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'b', 'a']),
        ('c', ['x', 'y', 'z', 'x'])
    ], index=[3, 4, 5, 8])

    df1 = df.copy()
    pdu.drop_columns(df1, 'a')

    pd_testing.assert_frame_equal(
        df1,
        pdu.from_items([
            ('b', ['a', 'b', 'b', 'a']),
            ('c', ['x', 'y', 'z', 'x'])
        ], index=[3, 4, 5, 8]))

    df2 = df.copy()
    pdu.drop_columns(df2, ['a', 'c'])
    pd_testing.assert_frame_equal(
        df2,
        pdu.from_items([
            ('b', ['a', 'b', 'b', 'a']),
        ], index=[3, 4, 5, 8]))

    with pytest.raises(KeyError):
        pdu.drop_columns(df, 'x')


def test_columns_to_right() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'b', 'a']),
        ('c', ['x', 'y', 'z', 'x'])
    ], index=[3, 4, 5, 8])

    df1 = pdu.columns_to_right(df, ['b', 'a'])
    pd_testing.assert_frame_equal(
        df1,
        pdu.from_items([
            ('c', ['x', 'y', 'z', 'x']),
            ('b', ['a', 'b', 'b', 'a']),
            ('a', [3, 4, 3, 2]),
        ], index=[3, 4, 5, 8]))


def test_shuffle_df_drop_index() -> None:
    df = pd.DataFrame(np.random.random(size=(3, 3)), columns=['a', 'b', 'c'])
    df1 = pdu.shuffle_df_drop_index(df)
    np.testing.assert_array_equal(df1.index.values, np.arange(len(df)))
    np.testing.assert_allclose(df1.sum(), df.sum())


def test_assert_frame_contents_equal() -> None:
    df1 = pdu.from_items([
        ('b', np.array([3, 8])),
        ('a', ['first', 'second']),
    ], index=[3, 4])

    df2 = pd.DataFrame([[3, 'first'], [8, 'second']],
                       columns=['b', 'a'])

    with pytest.raises(AssertionError):
        pd_testing.assert_frame_equal(df1, df2)

    pdu.assert_frame_contents_equal(df1, df2)


def test_ser_where_defined() -> None:
    x = pd.Series([4, 5, nan, 2, nan])

    pd_testing.assert_series_equal(
        pdu.ser_where_defined(x),
        pd.Series([4., 5, 2], index=[0, 1, 3]))


def test_n_undefined_and_percentage() -> None:
    x = pd.Series([4, 5, nan, 2, nan])

    n, perc = pdu.n_undefined_and_percentage(x)
    assert n == 2
    assert perc == 2 / 5 * 100


@pytest.mark.parametrize('ser, expected', [
    (pd.Series([3., nan, 4, nan]), 2),
    (pd.Series([3., 4]), 0),
    (pd.Series([None, "a", ""]), 1),
    (pd.Series(["a", ""]), 0),
    (pd.Series([]), 0),
])
def test_n_undefined(ser: pd.Series, expected: int) -> None:
    assert pdu.n_undefined(ser) == expected



@pytest.mark.parametrize('ser, expected', [
    (pd.Series([3., nan, 4, nan]), False),
    (pd.Series([3., 4]), True),
    (pd.Series([None, "a", ""]), False),
    (pd.Series(["a", ""]), True),
    (pd.Series([]), True),
])
def test_defined_everywhere(ser: pd.Series, expected: int) -> None:
    assert pdu.defined_everywhere(ser) == expected


@pytest.mark.parametrize('ser, expected', [
    (pd.Series([nan, 3., nan, 4, nan]), pd.Series([3., 3, 3, 4, 4])),
    (pd.Series([3., 4]), pd.Series([3., 4])),
    (pd.Series([None, "a", "", None]), pd.Series(["a", "a", "", ""])),
    (pd.Series(["a", ""]), pd.Series(["a", ""])),
    (pd.Series([]), pd.Series([])),
])
def test_fill_forward_then_backward(ser: pd.Series, expected: pd.Series) -> None:
    pd_testing.assert_series_equal(pdu.fill_forward_then_backward(ser), expected)


def test_colname_list() -> None:
    assert pdu.colname_list('foo') == ['foo']
    assert pdu.colname_list(['foo', 'bar']) == ['foo', 'bar']


def test_sort() -> None:
    df = pdu.from_items([
        ('a', [3, 4, 3, 2]),
        ('b', ['a', 'b', 'c', 'd']),
        ('c', ['x', 'y', 'z', 'w'])
    ], index=[3, 4, 5, 8])

    df1 = pdu.sort(df, colnames='a', inplace=True)
    assert df1 is df

    pd_testing.assert_frame_equal(
        df,
        pdu.from_items([
            ('a', [2, 3, 3, 4]),
            ('b', ['d', 'a', 'c', 'b']),
            ('c', ['w', 'x', 'z', 'y'])
        ], index=[0, 1, 2, 3]))


def test_sorted_unique_1dim() -> None:
    x = pd.Series([4, 3, nan, 8, 4, 3, nan, 2])
    pd_testing.assert_series_equal(
        pdu.sorted_unique_1dim(x),
        pd.Series([2, 3, 4, 8, nan]))


def test_left_merge() -> None:
    df = pdu.from_items([('ITEM', [10, 20, 70, 30]),
                         ('Quantity', [3, 4, 8, 9])])
    dfb = pdu.from_items([('ITEM', [10, 20, 90]),
                          ('Quantity_nrm', [8, 9, 7])])
    dfr = pdu.left_merge(df, dfb, on=['ITEM'])
    pd_testing.assert_frame_equal(
        dfr, pdu.from_items([('ITEM', [10, 20, 70, 30]),
                             ('Quantity', [3, 4, 8, 9]),
                             ('Quantity_nrm', [8, 9, nan, nan])]))

    df = pdu.from_items([('ITEM', np.zeros(0)),
                         ('Quantity', np.zeros(0))])
    dfb = pdu.from_items([('ITEM', np.zeros(0)),
                          ('Quantity_nrm', np.zeros(0))])
    dfr = pdu.left_merge(df, dfb, on=['ITEM'])
    pd_testing.assert_frame_equal(
        dfr, pdu.from_items([('ITEM', np.zeros(0)),
                             ('Quantity', np.zeros(0)),
                             ('Quantity_nrm', np.zeros(0))]
                             ))


@numba.njit
def add_cumsum_a_to_b(X: pd.DataFrame) -> None:
    a = X[:, 0]
    b = X[:, 1]
    b += np.cumsum(a)
    # to test whether overwriting a non-result column has any consequence:
    a[:] = 0.


@numba.njit
def double_a(X: pd.DataFrame) -> None:
    X[:, 0] *= 2


def test_fast_groupby_multi_transform() -> None:
    df = pdu.shuffle_df_drop_index(
        pdu.from_items([
            ('g', [0,   0, 0, 0, 1, 1, 1, 1]),
            ('a', [1,   2, 4, 8, 3, 9, 27, 81]),
            ('b', [nan, 2, 5, 4, 4, 0, 3, -1])
        ]))

    pdu.fast_groupby_multi_transform(
        df, 'g', ['a', 'b'], 'b', add_cumsum_a_to_b, further_sort_colnames='a')

    pdu.assert_frame_contents_equal(
        df,
        pdu.from_items([
            ('g', [0,   0, 0, 0,   1, 1, 1, 1]),
            ('a', [1,   2, 4, 8,   3, 9,  27, 81]),
            ('b', [nan, 5, 12, 19, 7, 12, 42, 119])
        ]))

    pdu.fast_groupby_multi_transform(
        df, 'g', 'a', 'a', double_a, already_sorted=True)

    pdu.assert_frame_contents_equal(
        df,
        pdu.from_items([
            ('g', [0,   0, 0, 0,   1, 1, 1, 1]),
            ('a', [2,   4, 8, 16,  6, 18, 54, 162]),
            ('b', [nan, 5, 12, 19, 7, 12, 42, 119])
        ]))


def test_flatten_multi_columns() -> None:
    df = pdu.from_items([
        (('a', '1'), [3, 4, 3, 2]),
        (('b', '2'), ['a', 'b', 'b', 'a']),
        (('c', '1'), ['x', 'y', 'z', 'x'])
    ], index=[3, 4, 5, 8])

    pdu.flatten_multi_columns(df)
    pd_testing.assert_frame_equal(
        df,
        pdu.from_items([
            ('a_1', [3, 4, 3, 2]),
            ('b_2', ['a', 'b', 'b', 'a']),
            ('c_1', ['x', 'y', 'z', 'x'])
        ], index=[3, 4, 5, 8]))


def test_rename_groupby_colnames() -> None:
    df = pdu.from_items([
        ('g', [0, 0, 0, 0, 1, 1, 1]),
        ('a', [2, 3, 0, 1, 4, 2, 1]),
        ('b', [-1, 1, 2, 0, -2, 1, 0]),
        ('c', [8, 2, 5, 1, -2, -1, 4]),
    ])

    dfg = df.groupby('g').agg(collections.OrderedDict([
        ('a', ['sum', 'max']),
        ('b', ['sum', 'count']),
        ('c', 'max'),
    ]))

    dfg1 = dfg.copy()
    pdu.rename_groupby_colnames(dfg1, name_for_count='group_count')
    pd_testing.assert_frame_equal(
        dfg1,
        pdu.from_items([
            ('a__sum', [6, 7]),
            ('a__max', [3, 4]),
            ('b', [2, -1]),
            ('group_count', [4, 3]),
            ('c', [8, 4])
        ], index=pd.Index([0, 1], name='g')))

    dfg2 = dfg.copy()
    pdu.rename_groupby_colnames(
        dfg2, name_for_count='group_count',
        renamings={'a__sum': 'summed_a', 'g': 'group', 'group_count': 'count'}
    )
    pd_testing.assert_frame_equal(
        dfg2,
        pdu.from_items([
            ('summed_a', [6, 7]),
            ('a__max', [3, 4]),
            ('b', [2, -1]),
            ('count', [4, 3]),
            ('c', [8, 4])
        ], index=pd.Index([0, 1], name='group')))


def test_print_column_info() -> None:
    ser = pd.Series([3, 4, nan, 2])

    out = io.StringIO()
    with pu.redirect_stdouterr(out, out):
        pdu.print_column_info(ser, table_name='X')


def test_print_table_info() -> None:
    df = pdu.from_items([
        ('a', [2, 3, 0, 1, 4, 2, 1]),
        ('c', [8, 2, 5, 1, -2, -1, 4]),
    ])

    out = io.StringIO()
    with pu.redirect_stdouterr(out, out):
        pdu.print_table_info(df, table_name='X')


def test_consistency_check() -> None:
    df = pdu.from_items([
        ('a', [2, 3,    0, 1, 4.1, 2, 1]),
        ('a1', [2, 3.1, 0, 1, 4,   2, 1]),
        ('c', [8, 2, 5, 1, -2, -1, 4]),
    ])

    out = io.StringIO()
    with pu.redirect_stdouterr(out, out):
        pdu.consistency_check(df, 'a', 'a1')


@pytest.mark.parametrize('entries', [
    ['2023-04-22 10:40:22', '2023-03-01 00:00:00'],
    ['2023-04-22', '2023-03-01', "NaT"],
])
def test_to_datetime_ser(entries: List[str]) -> None:
    pd_testing.assert_series_equal(
        pdu.to_datetime_ser(entries), pd.Series(pd.to_datetime(entries)))


def test_truncate_datetime_to_freq() -> None:
    x = pdu.to_datetime_ser(['2023-04-22 10:40:22', '2023-03-01 00:00:00'])

    pd_testing.assert_series_equal(
        pdu.truncate_datetime_to_freq(x, 'D'),
        pdu.to_datetime_ser(['2023-04-22', '2023-03-01']))

    pd_testing.assert_series_equal(
        pdu.truncate_datetime_to_freq(x, 'M'),
        pdu.to_datetime_ser(['2023-04-01', '2023-03-01']))

    pd_testing.assert_series_equal(
        pdu.truncate_datetime_to_freq(x, 'W'),
        pdu.to_datetime_ser(['2023-04-17', '2023-02-27']))


def test_truncate_datetime_to_month() -> None:
    df = pd.DataFrame({'dt': pd.to_datetime(['2017-09-12', '2017-10-20'])})

    df['dtm'] = pdu.truncate_datetime_to_month(df['dt'])

    pd_testing.assert_frame_equal(
        df, pdu.from_items([
        ('dt', pd.to_datetime(['2017-09-12', '2017-10-20'])),
        ('dtm', pd.to_datetime(['2017-09-01', '2017-10-01']))]))


def test_truncate_datetime_to_week() -> None:
    df = pd.DataFrame({'dt': pd.to_datetime(['2017-09-11', '2017-09-24'])})

    df['dtm'] = pdu.truncate_datetime_to_week(df['dt'])
    df['dtm_sun'] = pdu.truncate_datetime_to_week(df['dt'], sunday_first=True)

    pd_testing.assert_frame_equal(
        df, pdu.from_items([
            ('dt', pd.to_datetime(['2017-09-11', '2017-09-24'])),
            ('dtm', pd.to_datetime(['2017-09-11', '2017-09-18'])),
            ('dtm_sun', pd.to_datetime(['2017-09-10', '2017-09-24']))
        ]))


def test_datetime_to_epoch() -> None:
    pd_testing.assert_series_equal(
        pdu.datetime_to_epoch(
            pdu.to_datetime_ser(
                ["1970-01-01 00:00:00.0", "1970-01-01 0:01:02.345", "NaT"])),
        pd.Series([0., 62.345, nan]), check_exact=True)

    pd_testing.assert_series_equal(
        pdu.datetime_to_epoch(
            pdu.to_datetime_ser(["1970-01-01 1:00:00"])),
        pd.Series([3600.]))


def test_convert_to_timezone() -> None:
    ser = pdu.to_datetime_ser(
        ['2022-02-01 23:05:00', '2022-06-05 10:20:00'])
    ser_berlin = pdu.convert_to_timezone(ser, 'Europe/Helsinki')
    pd_testing.assert_series_equal(
        ser_berlin.dt.day, pd.Series([2, 5], dtype=np.int32))
    pd_testing.assert_series_equal(
        ser_berlin.dt.hour, pd.Series([1, 13], dtype=np.int32))
    pd_testing.assert_series_equal(
        ser_berlin.dt.minute, pd.Series([5, 20], dtype=np.int32))


def test_add_missing_days_one_level() -> None:
    df = pdu.from_items([
        ('date', pd.to_datetime(['2020-02-01', '2020-02-03'])),
        ('a', [2, 3])
    ]).set_index('date')

    expd = pdu.from_items([
        ('date',
         pd.to_datetime(['2020-02-01', '2020-02-02', '2020-02-03',
                         '2020-02-04', '2020-02-05'])),
        ('a', [2, nan, 3, nan, nan])])

    pd_testing.assert_frame_equal(
        pdu.add_missing_days(df, end_datetime='2020-02-05'),
        expd)

    pd_testing.assert_frame_equal(
        pdu.add_missing_days(df, end_datetime='2020-02-05', reset_index=False),
        expd.set_index('date'))

    pd_testing.assert_frame_equal(
        pdu.add_missing_days(df),
        pdu.from_items([
            ('date',
             pd.to_datetime(['2020-02-01', '2020-02-02', '2020-02-03'])),
            ('a', [2, nan, 3])]))


def test_add_missing_days_multiple_levels() -> None:
    df = pdu.from_items([
        ('a', [0, 0, 0, 1, 1]),
        ('date',
         pd.to_datetime([
             '2023-07-03', '2023-07-03', '2023-07-17',
             '2023-07-03', '2023-07-17'])),
        ('c', [5, 6, 5, 5, 6]),
        ('d', [10, 11, 12, 13, 14])
    ]).set_index(['a', 'date', 'c'])

    print(
        pdu.add_missing_days(df, '2023-07-31', freq='W-MON'))
    pd_testing.assert_frame_equal(
        pdu.add_missing_days(df, '2023-07-31', freq='W-MON'),
        pdu.from_items([
            ('a', [0] * 10 + [1] * 10),
            ('date',
             pd.to_datetime((
                 ['2023-07-03'] * 2 + ['2023-07-10'] * 2 + ['2023-07-17'] * 2
                 + ['2023-07-24'] * 2 + ['2023-07-31'] * 2
             ) * 2)),
            ('c', [5, 6] * 10),
            ('d', [10, 11, nan, nan, 12, nan, nan, nan, nan, nan,
                   13, nan, nan, nan, nan, 14, nan, nan, nan, nan]),
        ]))


def test_to_csv() -> None:
    df = pdu.from_items([
        ('b', np.array([3, 8])),
        ('a', ['first', 'second']),
    ], index=[3, 4])

    out = io.StringIO()
    pdu.to_csv(df, out)

    assert out.getvalue() == "b;a\n3;first\n8;second\n"


