Data and code associated with: What Came First?
Wright AM, Lyons KM, Hillis DM, Brandley MB.
=========

+ Exploratory notebooks: IPython notebooks used for exploratory analysis. These scripts are not used in the main pipeline, but used to explore data. Values from these exploratory notebooks are reported in the paper, but not used explicitly a pipeline step. Also included are interactive vesions of pipeline pieces.
+ Main pipeline: This is the main pipeline used to create the main results in the paper. Makefile reproduces full analysis. To do this, clone the repository, change directories into it and type `make`
+ Dependencies:
    + R:
        + Diversitree
    + Python:
        + Pandas
        + Matplotlib
        + Dendropy
        
+ Note: Running the full pipeline with make is a multiple-hour process. Picking the steps of interest out of the Scripts directory is almost certainly more useful.

## Installing Dependencies

### Installing diversitree

Install gsl (pre-requisite)

```console
$ sudo apt-get install gsl-bin libgsl0-dev
```

Now install diversitree

```R
install.packages(c('diversitree'))
```
