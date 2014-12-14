FROM ipython/scipystack

RUN apt-get install -y r-base r-base-dev r-cran-rcurl libreadline-dev

RUN useradd -m -s /bin/bash squamate

USER squamate
ENV HOME /home/squamate
ENV SHELL /bin/bash
ENV USER squamate

WORKDIR /home/squamate

# Setup the R environment
RUN echo 'R_LIBS_USER=~/.R:/usr/lib/R/site-library' > /home/squamate/.Renviron
RUN echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com")))' > /home/squamate/.Rprofile

RUN mkdir /home/squamate/.R/

RUN echo "install.packages(c('RCurl', 'devtools'))" | R --no-save

RUN chown -R squamate:squamate /home/squamate
