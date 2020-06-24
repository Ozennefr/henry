FROM python:3.8.2-buster AS base
LABEL maintainer="Ozenne Francois <francois.ozenne@gmail.com>"
# user setup
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME
# Python env setup
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV="/home/$USERNAME/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#python project setup
ENV PYTHONPATH="/henry/src"
WORKDIR /henry


FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.5
RUN sudo pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./


FROM builder as dev
RUN poetry install


FROM builder as requirements
RUN poetry install --no-dev


FROM base as release
COPY --chown=$USERNAME:$USERNAME --from=requirements $VIRTUAL_ENV $VIRTUAL_ENV
CMD ["sleep", "infinity"]

