# Joblog

The Joblog library provides a simple logging system. It’s ideal for batch jobs but can also be used
for longer running systems.

## Features

* Log format compatible with [Google Logging Library](https://github.com/google/glog).
* Log files are automatically written to a directory tree arranged by date with unique names.
* Available for several programming languages.
* Status lines logged automatically at start and exit.

## Example

This example demonstrates many of the features:

```
$ node example.js
I0127 160235.292 [20M] logging to logs/2016/201601/20160127/20160127_160235_example_6232_pocitac.log
I0127 160235.304 [21M] start example: node v4.2.6 linux, hostname pocitac, user james
I0127 160235.306 [21M] invoked as: /usr/bin/nodejs /home/james/Projects/joblog/example.js --run

I0127 160235.307 [21M] running example
I0127 160235.312 [22M] processed 100000/1324025 (7.6%), sum 4957425
I0127 160235.316 [22M] processed 200000/1324025 (15.1%), sum 9910422
I0127 160235.319 [22M] processed 300000/1324025 (22.7%), sum 14858261
I0127 160235.321 [22M] processed 400000/1324025 (30.2%), sum 19814380
I0127 160235.324 [22M] processed 500000/1324025 (37.8%), sum 24758867
I0127 160235.326 [22M] processed 600000/1324025 (45.3%), sum 29711562
I0127 160235.328 [22M] processed 700000/1324025 (52.9%), sum 34665519
I0127 160235.330 [22M] processed 800000/1324025 (60.4%), sum 39619914
I0127 160235.333 [22M] processed 900000/1324025 (68.0%), sum 44573943
I0127 160235.335 [22M] processed 1000000/1324025 (75.5%), sum 49515369
I0127 160235.337 [22M] processed 1100000/1324025 (83.1%), sum 54484107
I0127 160235.339 [22M] processed 1200000/1324025 (90.6%), sum 59447012
I0127 160235.341 [22M] processed 1300000/1324025 (98.2%), sum 64397686
I0127 160235.342 [22M] processed 1324025/1324025 (100.0%), sum 65590458
W0127 160235.342 [22M] final sum 65590458

I0127 160235.346 [22M] exit example: pid 6232, real 0.059s, user 0.00s, system 0.00s, read 31K, written 2K, peak rss 22M
```

* The log is written to standard error as well as to the log file.
* All times are in UTC.
* The format is "<level><month/day> <time> [RSS] message".
* The log file name contains the date, time, program name, pid, and hostname. The resulting tree is
  safe to rsync to a central store where it will not overwrite logs from other jobs or machines.
* The first lines show the environment and command line.
* The last line shows run time, IO stats, and memory usage.

## Usage

### Javascript (Node)

```
npm install joblog
```

```
var joblog = require("joblog");
joblog.info("processed %i/%i", i + 1, total);
joblog.warn("final sum %i", sum);
```

### Python

```
pip3 install git+https://github.com/jamesbursa/joblog
```

```
import joblog
import logging

joblog.init()  # Optional: supply logs_dir="...".
logging.info("%i/%i (%.1f%%) processed", i + 1, total, 100.0 * (i + 1) / total)
logging.warn("all done")
```

Compatible with Python 2 and 3.
