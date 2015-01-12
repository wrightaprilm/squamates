FROM ipython/scipystack

RUN apt-get install -y r-base r-base-dev r-cran-rcurl libreadline-dev
RUN apt-get install gsl-bin libgsl0-dev

RUN pip2 install dendropy

RUN useradd -m -s /bin/bash squamate

USER squamate
ENV HOME /home/squamate
ENV SHELL /bin/bash
ENV USER squamate

# Setup the R environment
RUN echo 'R_LIBS_USER=~/.R:/usr/lib/R/site-library' > /home/squamate/.Renviron
RUN echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com")))' > /home/squamate/.Rprofile

RUN mkdir /home/squamate/.R/

# R dev helpers
RUN echo "install.packages(c('RCurl', 'devtools'))" | R --no-save
RUN echo "install.packages(c('diversitree'))" | R --no-save

USER root
ADD . /home/squamate/squamates
RUN chown -R squamate:squamate /home/squamate
USER squamate

WORKDIR /home/squamate/squamates

CMD ["make"]
