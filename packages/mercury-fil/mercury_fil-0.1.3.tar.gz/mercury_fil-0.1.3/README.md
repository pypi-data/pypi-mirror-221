# mercury-py

`mercury-py` is a Python package that simplifies
working with historical Filecoin chain data stored on BigQuery.

The results from the Mercury client are `pandas.DataFrame` objects.

## prerequisites

Install the `gcloud` CLI.

For `homebrew` users: 

```sh
brew install --cask google-cloud-sdk
```

Other installation methods are [here](https://cloud.google.com/sdk/docs/install).

## installation

`pip install mercury-fil`

## usage

Make sure you're authenticated: `gcloud auth login`. 
You'll also need to be in the right project: `gcloud config set project protocol-labs-data`.

> 💡 Only query for columns (and the height range) that you need.
> A query costs $6.25/TB.

### simple api

The `fevm_contracts` and `derived_gas_outputs` methods only have
2 required arguments, namely the `start_height` and `end_height`. 

It's financially costly to query all of the heights so make sure
that you **only query for heights that you need**. The tables
are partitioned in BigQuery by `height` at intervals of `3000`.

The API defaults to a dry run so it computes the bytes it will
process before you decide whether to run the query job.

```py3
>>> from mercury import Client
>>> client = Client()
>>> df = client.fevm_contracts(start_height=2683348, end_height=2683348+2880)
>>> df
'0.1322889 GiB'
>>> df = client.fevm_contracts(start_height=2683348, end_height=2683348+2880, dry_run=False)
       height                                 eth_address                                          byte_code                         balance
0     2684783  0x8b9ebed1f4a0892097b913ba938c069330652947  60806040526004361061004a5760003560e01c806363a5...                            0E-9
1     2684264  0x719e14fcb364bb05649bd525eb6c4a2d0d4ea2b7  6080604052600436106100a05760003560e01c8063313c...   2212000000000000000.000000000
2     2684238  0x719e14fcb364bb05649bd525eb6c4a2d0d4ea2b7  6080604052600436106100a05760003560e01c8063313c...   2211000000000000000.000000000
3     2684210  0x719e14fcb364bb05649bd525eb6c4a2d0d4ea2b7  6080604052600436106100a05760003560e01c8063313c...   1211000000000000000.000000000
4     2684204  0x719e14fcb364bb05649bd525eb6c4a2d0d4ea2b7  6080604052600436106100a05760003560e01c8063313c...   1201000000000000000.000000000
...       ...                                         ...                                                ...                             ...
3657  2685897  0x8f81929b4b8e0a76d13e90dfb5d2316a4a163d26  6080604052600436106101e35760003560e01c80635c97...  58400000000000000000.000000000
3658  2685891  0x8f81929b4b8e0a76d13e90dfb5d2316a4a163d26  6080604052600436106101e35760003560e01c80635c97...  57400000000000000000.000000000
3659  2685887  0x8f81929b4b8e0a76d13e90dfb5d2316a4a163d26  6080604052600436106101e35760003560e01c80635c97...  53400000000000000000.000000000
3660  2685716  0x8f81929b4b8e0a76d13e90dfb5d2316a4a163d26  6080604052600436106101e35760003560e01c80635c97...  49400000000000000000.000000000
3661  2685132  0x8f81929b4b8e0a76d13e90dfb5d2316a4a163d26  6080604052600436106101e35760003560e01c80635c97...  47400000000000000000.000000000

[3662 rows x 4 columns]

>>> df = client.derived_gas_outputs(start_height=0, end_height=2880, dry_run=False)
>>> df
        height                                               from      to           value  method   gas_used
0          315  f3ro3i54tule2vtdcsjdkzjkf6djx3wwe5znv5h4kwxprx...     f05            0E-9       4   29167738
1         2150  f3sqdk3xwrfrxb77upn4jjnqzamoiuzmykavyguodsmxgh...     f05            0E-9       4   39859680
2         2119  f3qcagyij6lb7ixssn5vxgrqekike2ujcn7b7v5jci4foq...     f05            0E-9       4   42993922
3         1743  f3r6vel3cnsvc4ct2zymfxorxz5by4rc5tuwjb3ykbl4cn...  f07919  1000.000000000       5  382976458
4         2592  f3qjn4pqvipuaxyjigcbzp4zn5625646ogbqwuzmakgx5q...  f03362  1000.000000000       5  380578332
...        ...                                                ...     ...             ...     ...        ...
675645     342  f3uxgextdo6bmkn5ax3gtfn6t3j3js5ywnojwpmc7suhyp...     f04            0E-9       2   16488846
675646     342  f3uxgextdo6bmkn5ax3gtfn6t3j3js5ywnojwpmc7suhyp...     f04            0E-9       2   16844158
675647     342  f3uxgextdo6bmkn5ax3gtfn6t3j3js5ywnojwpmc7suhyp...     f04            0E-9       2   16563776
675648     342  f3uxgextdo6bmkn5ax3gtfn6t3j3js5ywnojwpmc7suhyp...     f04            0E-9       2   16691916
675649    2051          f16aum7jrmrwa7aqr2d5feu7on4emsgqh2gmxdf7q     f04            0E-9       2   16382158

[675650 rows x 6 columns]
```

### selecting columns

BigQuery is a columnar data store, which means that the data is stored
on disk by column. For example, the `derived_gas_outputs.method` column
would be stored like so:

```
| method | 4 | 4 | 4 | 5 | 5 | 2 | 2 |
```

It is thus more efficient to read many records in a table by column.
Since a column usually has a non-insignificant amount of data (in bytes), 
the query can become costly if you select all the columns of a table.
The financial cost is a reason why the default columns in the `fevm_contracts`
and `derived_gas_outputs` methods do not contain all of the columns listed in 
[`lilium.sh`](https://lilium.sh/data/chain/).

To select the columns you need, you need to pass a 
[tuple](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
of those column names. For example:

```py3
>>> df = client.fevm_contracts(start_height=2683348, end_height=2683348+2880, columns=("height", "actor_id", "byte_code_hash"), dry_run=False)
>>> df
       height                                      actor_id                                     byte_code_hash
0     2684783  f410fropl5upuucesbf5zco5jhdagsmygkkkhgifa3pi  36cdf3ab5e4b065b46d89eb1b595da8acdbb725520983d...
1     2684264  f410fogpbj7ftms5qkze32us6w3ckfugu5ivx4eoycoi  af58eb543e44897848df115f2276f7b5ffc12fa068de8c...
2     2684238  f410fogpbj7ftms5qkze32us6w3ckfugu5ivx4eoycoi  af58eb543e44897848df115f2276f7b5ffc12fa068de8c...
3     2684210  f410fogpbj7ftms5qkze32us6w3ckfugu5ivx4eoycoi  af58eb543e44897848df115f2276f7b5ffc12fa068de8c...
4     2684204  f410fogpbj7ftms5qkze32us6w3ckfugu5ivx4eoycoi  af58eb543e44897848df115f2276f7b5ffc12fa068de8c...
...       ...                                           ...                                                ...
3657  2685897  f410fr6azfg2lryfhnuj6sdp3lurrnjfbmpjgwco5svi  a48a535d2921613878ca9393b62022db4e2caaafd5a23f...
3658  2685891  f410fr6azfg2lryfhnuj6sdp3lurrnjfbmpjgwco5svi  a48a535d2921613878ca9393b62022db4e2caaafd5a23f...
3659  2685887  f410fr6azfg2lryfhnuj6sdp3lurrnjfbmpjgwco5svi  a48a535d2921613878ca9393b62022db4e2caaafd5a23f...
3660  2685716  f410fr6azfg2lryfhnuj6sdp3lurrnjfbmpjgwco5svi  a48a535d2921613878ca9393b62022db4e2caaafd5a23f...
3661  2685132  f410fr6azfg2lryfhnuj6sdp3lurrnjfbmpjgwco5svi  a48a535d2921613878ca9393b62022db4e2caaafd5a23f...

[3662 rows x 3 columns]
```

As with querying only data at the range of heights that you need, **only
select columns that you need.**

### supported tables

- `fevm_contracts`
- `derived_gas_outputs`
- `miner_sector_events`
- `miner_sector_infos`

## contributing

To contribute, you'll need [Poetry](https://python-poetry.org/docs/#installing-with-pipx) 
to install the dependencies.

To run the tests, simply run `pytest`.
