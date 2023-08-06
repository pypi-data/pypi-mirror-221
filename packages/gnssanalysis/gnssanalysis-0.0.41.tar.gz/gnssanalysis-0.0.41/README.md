# gnssanalysis
The package encompasses various GNSS-related functionality such as efficient reading and writing GNSS files (e.g. SINEX, SP3, CLK, IONEX and many others), advanced analysis and comparison, various coordinate transformations including geodetic frame rotations, predictions and combinations.
Package  Solver.

## Install

```bash
pip install gnssanalysis
```



### File formats supported
- BLQ
- BSX/BIA
- CLK
- ERP
- IONEX
- NANU
- RINEX
- SINEX (including discontinuity, post-seismic file formats)
- SP3
- TROP
- GINAN proprietary formats: PEA partials, POD output, STEC and TRACE

# Standalone utilities
There is a set of standalone utilities installed together with the module module which are build on top of gnssanalysis.

## diffutil
A utility originally created for automated testing of the computed GNSS files relative to the known good solution files.
The simplest use case for the `diffutil` is to call it with two GNSS files specified after `-i`:
```bash
diffutil -i file1 file2
```
`diffutil` parses files' extensions and automatically calls a command needed, e.g. `sp3` for `file.sp3`. It is also possible to specify the command manually in case file extensions are non-standard or missing.

```bash
diffutil -i file1 file2 sp3 # sp3 is a command inside diffutil
```

## snxmap
Reads any number of sinex files given, specifically the SITE/ID block and creates an interactive html map with all the stations plotted. Every file will get a unique color marker, with decreasing size for each additional marker, constructing "lollipops" at common stations. This allows seeing intersections of stations within files to be easily seen.
The sinex files may also be compressed (either .Z or .gz)

How to use:
```bash
snxmap snxfile1 snxfile2.Z snxfile3.gz
```
`-o path_to_output`

## sp3merge
Merges any number of sp3 files together creating sp3 file of any length. Could also accept clk files to populate merged sp3 with clock offset values.

How to use:
```bash
sp3merge -s file1.sp3 file2.sp3.Z file3.sp3.gz -c file1.clk file2.clk.Z file3.clk.gz
```
## log2snx
A utility to parse collection of igs-format station files and create a sinex file with required station information - location, station hardware etc. 

How to use:
```bash
log2snx -l "~/logfiles/*/*log"
```


## trace2mongo (needs update)
Converts tracefile to the mongo database that is compatible with Ginan's mongo output for EDA

## gnss-filename
Determines appropriate filename for GNSS based on the content


## orbq
Compares two sp3 files and outputs statistics to the terminal window.

How to use:
```bash
orbq -l "~/logfiles/*/*log"
```


# Some usage examples

## Combination of sinex solutions files
Combination of with a frame file projected to a midday of a date of interest
Usage examples:

- Daily comnination with frame_of_day centered at midday
```python
from gnssanalysis import gn_combi
daily_comb_neq = gn_combi.addneq(snx_filelist=_glob.glob('/data/cddis/2160/[!sio][!mig]*0.snx.Z'),frame_of_day=frame_of_day)
```

- Weekly combination with frame_of_day centered at week's center:
```python
weekly_comb_neq = gn_combi.addneq(snx_filelist=_glob.glob('/data/cddis/2160/[!sio][!mig]*.snx.Z'),frame_of_day=frame_of_day)
```

 The frame of day could be generated using a respective function from `gn_frame` module:
 ```python
from gnssanalysis import gn_frame, gn_datetime

frame_datetime = gn_datetime.gpsweeksec2datetime(2160,43200)

frame_of_day = gn_frame.get_frame_of_day(date_or_j2000=frame_datetime, itrf_path_or_df = '/data/cddis/itrf2014/ITRF2014-IGS-TRF.SNX.gz',discon_path_or_df='/data/cddis/itrf2014/ITRF2014-soln-gnss.snx',psd_path_or_df='/data/cddis/itrf2014/ITRF2014-psd-gnss.snx')
 ```