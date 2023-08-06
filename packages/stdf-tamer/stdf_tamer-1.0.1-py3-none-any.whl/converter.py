"""export stdf data to more usefull format.

Usage:
  convertstdf --output=<output> --stdf-in=<stdf-in> [--compression=<zstd>]

Options:
  -h --help     Show this screen.
"""
import ams_rw_stdf
import bz2
import construct
from docopt import docopt
import gzip
import pathlib
import polars as pl
from rich.console import Console


console = Console()
err_console = Console(stderr=True, style="bold red")
_opener = {"bz2": bz2.open, "gz": gzip.open, "stdf": open}


schema = {'Test_Nr': pl.Int64,'Test_Name': pl.Categorical, 'ULim': pl.Float64, 
          'LLim': pl.Float64, 'res': pl.Float64, 'lot_id': pl.Categorical, 
          'TEST_COD': pl.Categorical, 'operator': pl.Categorical, 'START_T': pl.Int64, 
          'part_id': pl.Categorical, 'part_txt': pl.Categorical}

output_writers = {".ipc":     lambda df, outpath, compression: df.write_ipc(outpath, compression=compression),
                  ".feather": lambda df, outpath, compression: df.write_ipc(outpath, compression=compression),
                  ".parquet": lambda df, outpath, compression: df.write_parquet(outpath, compression=compression),
                  ".xlsx":    lambda df, outpath, compression: df.write_excel(outpath)}

def main():
    try:
        arguments = docopt(__doc__)
        outpath = pathlib.Path(arguments["--output"])
        def worker():
            si = arguments["--stdf-in"]
            ftype = si.split(".")[-1]
            if ftype not in _opener:
                err_console.print(f"{ftype} is an unsupported file extension, only {', *.'.join(_opener.keys())} are supported")
            if outpath.suffix not in output_writers:
                err_console.print(f"please use one of these file formats as output: {', *'.join(output_writers.keys())}")
            with _opener[ftype](si, "rb") as f:
                data = None
                operator = None
                test_cod = None
                lot_id  = None
                start_t = None
                while True:
                    try:
                        c = ams_rw_stdf.parse_record(f)
                    except construct.core.StreamError as e:
                        if "stream read less than specified amount, expected 2, found 0" not in str(e):
                            err_console.print_exception()
                        break
                    except Exception as e:
                        err_console.print(f"Parsing issue")
                        err_console.print_exception()
                        break
                    if c.REC_TYP == 15 and c.REC_SUB == 10:
                        data["Test_Nr"].append(c.PL.TEST_NUM)
                        data["Test_Name"].append(c.PL.TEST_TXT)
                        data["ULim"].append(c.PL.HI_LIMIT)
                        data["LLim"].append(c.PL.LO_LIMIT)
                        data["res"].append(c.PL.RESULT)
                        
                    if c.REC_TYP == 1 and c.REC_SUB == 10:
                        test_cod = str(c.PL.TEST_COD)
                        lot_id   = c.PL.LOT_ID
                        operator = c.PL.OPER_NAM
                        start_t = c.PL.START_T
                        data = {"Test_Nr": [], "Test_Name": [], "ULim": [], "LLim": [], "res": [], "lot_id": lot_id,  "TEST_COD": test_cod, "operator": operator, "START_T": start_t}
                        console.print(f"Converting LOT ID: '{lot_id}' measurments to {arguments['--output']}...")
                        
                    if c.REC_TYP == 5 and c.REC_SUB == 20:
                        data["part_id"] = c.PL.PART_ID
                        data["part_txt"] = c.PL.PART_TXT
                        console.print(f"Adding part {c.PL.PART_TXT}/{c.PL.PART_ID}")
                        yield pl.DataFrame(data, schema=schema)
                        data = {"Test_Nr": [], "Test_Name": [], "ULim": [], "LLim": [], "res": [], "lot_id": lot_id,  "TEST_COD": test_cod, "operator": operator, "START_T": start_t}
        with pl.StringCache():
            df = pl.concat(worker())
        
        output_writers[outpath.suffix](df, outpath, compression=arguments["--compression"])
    except Exception as e:
        err_console.print_exception()


if __name__ == "__main__":
    main()
