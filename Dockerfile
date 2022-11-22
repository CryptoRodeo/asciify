FROM python:3.10

WORKDIR /code

ARG USER=snek
ARG UID=1000
ARG GID=1000
ARG PW=snek

COPY . .

# Create user "snek" with UID 1000
RUN useradd -m ${USER} --uid=${UID} && \
# Update user's password
echo "${USER}:${PW}" | chpasswd

# Change group ownership of all the files to this user
RUN chgrp -R ${GID} ./

ENV VIRTUAL_ENV=/code/venv
# create virtualenv, activate it
RUN python3 -m venv ${VIRTUAL_ENV}
# add virtualenv/bin to the path
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# update pip, install packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Set user for the image
USER ${USER}

ENTRYPOINT ["./app.sh"]